import requests
import pytest
from copy import deepcopy
import allure
from models.user import UserLoginData, User


API_BASE = 'https://qauto2.forstudy.space/api/'


class DataUserProfileGet:
    def __init__(self, user_id, photo_file_name, name, last_name,):
        self.userId = user_id
        self.photoFilename = photo_file_name
        self.name = name
        self.lastName = last_name

    def __str__(self):
        return self.__dict__


class UserProfileGet:
    def __init__(self, status: str, data: DataUserProfileGet):
        self.status = status
        self.data = data.__dict__


def log_requests_session(r, *args, **kwargs):
    req = r.request
    allure.attach(req.body or '', name=f"API request {req.method} {req.url}",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(r.text or '', name=f"API reply {r.status_code} {r.reason}",
                  attachment_type=allure.attachment_type.JSON)


class TestRegister:
    def setup_class(self):
        self.session = requests.session()
        self.session.hooks['response'].append(log_requests_session)

        user_to_login = UserLoginData("test@tesster.com", "Qwerty12345", False)
        self.user = User(API_BASE, self.session, 'TestName', 'TestLastName', user_to_login)

    @allure.title("test_user_register: Check valid user registration")
    @allure.description("Verifying, that a user can be successfully registered with valid data.")
    def test_user_register(self):
        result = self.user.register()
        self.user.delete()
        assert result['status'] == 'ok'
        self.response = result

    # iterate over UserRegisterData fields
    @pytest.mark.parametrize('field_name', [
        'name', 'lastName', 'email', 'password', 'repeatPassword'])
    def test_user_register_empty_fields(self, field_name):
        fields = {
            'name': "Name",
            'lastName': "Last Name",
            'email': "Email",
            'password': "Password",
            'repeatPassword': "Repeat Password",
        }

        field_title = fields[field_name]
        allure.dynamic.title(f"test_user_register_empty_fields [{field_name}]")
        allure.dynamic.description(f"Verifying, that registration fails when the {field_title} field is empty.")

        # deepcopy to avoid self.user modifications
        malformed_user = deepcopy(self.user)

        # set empty field
        setattr(malformed_user.user_register, field_name, '')

        result = malformed_user.register()

        # delete it in cases we got 'ok'
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == f'"{field_name}" is not allowed to be empty'

    @allure.title("test_user_register_wrong_name: Check incorrect name format registration failure")
    @allure.description("Verifying, that registration fails when using an incorrect format for the name field.")
    def test_user_register_wrong_name(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.name = 'wrong_name'

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == 'Name is invalid'

    @allure.title("test_user_register_wrong_lastname: Check incorrect last name format registration failure")
    @allure.description("Verifying, that registration fails when using an incorrect format for the last name field.")
    def test_user_register_wrong_lastname(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.lastName = 'wrong_last_name'

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == 'Last Name is invalid'

    @pytest.mark.parametrize('pwd,title,desc', [
        ('test', "Short", "short password of 'test'."),
        ('t1T', "Invalid Characters", "invalid password containing 't1T'."),
        ('t' * 20, "Long", "long password of 20 't's."),
        pytest.param('t' * 10, "Medium-Length Invalid", "medium-length password of 10 't's.",
                     marks=pytest.mark.xfail(reason="Is expected to be failed coz API has bug in the "
                                                    "password field validator")),
    ])
    def test_user_register_wrong_password(self, pwd, title, desc):
        allure.dynamic.title(f"test_user_register_wrong_password [{pwd}]")
        allure.dynamic.description(f"Verifying that the system correctly handles user registration with a {desc}")

        malformed_user = deepcopy(self.user)
        malformed_user.user_register.password = pwd

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == ('Password has to be from 8 to 15 characters long '
                                     'and contain at least one integer, one capital, and one small letter')

    @allure.title("test_user_register_passwords_do_not_match: Check non-matching passwords registration failure")
    @allure.description("Verifying, that registration fails when the password and repeatPassword fields do not match.")
    def test_user_register_passwords_do_not_match(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_register.repeatPassword = 'test'

        result = malformed_user.register()
        if result['status'] == 'ok':
            malformed_user.delete()

        assert result['status'] == 'error'
        assert result['message'] == 'Passwords do not match'

    def teardown_class(self):
        self.user.login()
        self.user.delete()


class TestAuth:
    def setup_class(self):
        self.session = requests.session()

        user_to_login = UserLoginData("test@tesster.com", "Qwerty12345", False)
        self.user = User(API_BASE, self.session, 'TestName', 'TestLastName', user_to_login)

        self.user.register()
        self.user.logout()

    def setup_method(self):
        result = self.user.login()
        # save for profile tests
        self.user_id = result['data']['userId']

    @allure.title("test_user_login: Check valid user login")
    @allure.description("Verifying, that a user can log in successfully with valid credentials.")
    def test_user_login(self):
        self.user.logout()
        result = self.user.login()
        assert result["status"] == "ok"

    @allure.title("test_user_login_wrong_email: Check incorrect email login failure")
    @allure.description("Verifying, that login fails when using an incorrect email address.")
    def test_user_login_wrong_email(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_login.email = 'wrong_user@domain.invalid'
        self.user.logout()
        result = malformed_user.login()

        assert result["status"] == "error"
        assert result["message"] == "Wrong email or password"

    @allure.title("test_user_login_wrong_password: Check incorrect password login failure")
    @allure.description("Verifying, that login fails when using an incorrect password.")
    def test_user_login_wrong_password(self):
        malformed_user = deepcopy(self.user)
        malformed_user.user_login.password = 'wrong_pass'
        self.user.logout()
        result = malformed_user.login()
        assert result["status"] == "error"
        assert result["message"] == "Wrong email or password"

    @allure.title("test_check_user_profile: Check user profile retrieval")
    @allure.description("Verifying the retrieval of user profile information.")
    def test_check_user_profile(self):
        result = self.user.get_profile()

        data = DataUserProfileGet(self.user_id, 'default-user.png',
                                  self.user.user_register.name,
                                  self.user.user_register.lastName)

        profile = UserProfileGet('ok', data)

        assert result["data"] == profile.data
        assert result["status"] == profile.status

    def teardown_method(self):
        self.user.logout()

    def teardown_class(self):
        self.user.login()
        self.user.delete()
