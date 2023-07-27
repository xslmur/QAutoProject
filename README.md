[![run qauto tests](https://github.com/xslmur/login_auto_testing/actions/workflows/test.yml/badge.svg)](https://github.com/xslmur/login_auto_testing/actions/workflows/test.yml)

## ⬇️ Test plan for ‘Garage’ # 1.0

|          |             |                 |            |
| :------: | :---------: |:---------------:|:----------:|
| **Date** | **Version** | **Description** | **Author** |
| 07.07.23 |     1.0     |  Stage 1. - 4.  |  Karoline  |

- 1\. [Introduction](#intro)
  - 1.1 [General Information](#intro_general)
  - 1.2 [Testing Methods](#test_methods)
  - 1.3 [References](#references)
- 2\. [Preconditions](#preconditions)
- 3\. [Test Strategy](#test_strategy)
  - 3.1 [Testing objects](#testing_objects)
  - 3.2 [Description of the testing elements](#description_elem)
  - 3.3 [Functionality and key features to be tested](#tested_features)
  - 3.4 [Checklist and Test Cases for Login Pop-up](#checklist)
- 4\. [Test Environment](#environment)
  
-----
<a name="intro" />

### 1. Introduction
This document describes the plan for testing the home page of the HillelQAuto [Hillel QAuto](https://qauto.forstudy.space/).

Our website test automation project, [Hillel QAuto](https://qauto.forstudy.space/),
aims to create a reliable and efficient testing process to ensure this
resource's high quality and consistent performance.
The website provides training material and tools for learning automated testing,
and our goal is to test the performance and functionality of each of these tools.
The main goal of our project is to provide reliable and accurate functionality testing
of the [Hillel QAuto](https://qauto.forstudy.space/) website.
We plan to automate the testing of various features and modules.

-----
<a name="intro_general" />

### 1.1 General Information

This application was created for teaching purposes for Hillel students to improve their knowledge about software testing and development. This application is used by many students related to different areas of study (testers, developers, and so on). That's why it must be available and workable 24 hours a day, 7 days a week. It's essential for the application to be created according to the main requirements for applications of this type, but at the same time contained a number of non-primitive errors for supporting the learning process.

-----
<a name="test_methods" />

### 1.2 Testing Methods: Selenium WebDriver and API for Hillel QAuto

To achieve our testing objectives effectively, we have chosen to leverage two essential tools in the software testing domain: Selenium WebDriver and API testing. The integration of these two technologies enables us to conduct comprehensive testing, encompassing both the front-end and back-end aspects of the website. <br/>
Selenium WebDriver will be employed to automate the functional testing of the website's user interface. With its capabilities to interact with the website as an end-user would, we can assess the behavior of the website across different web browsers and platforms, ensuring a consistent experience for all users. <br/>
In addition to the front-end testing, API testing will play a pivotal role in evaluating the functionality and responses of various API endpoints utilized by the Hillel QAuto website. This backend testing approach enables us to verify the correctness and reliability of the website's interaction with its underlying services. <br/>
Through the amalgamation of Selenium WebDriver and API testing, we aim to achieve an encompassing and robust testing process, yielding a website that not only meets but exceeds the expectations of its users. Our focus on automation will contribute to an efficient and repeatable testing process, allowing us to continually monitor and maintain the website's performance and functionality. <br/>
By meticulously adhering to this testing plan, we are confident in delivering a top-tier user experience on the Hillel QAuto website, ensuring that it remains a reliable and valuable resource for those interested in automated testing methodologies.

-----

<a name="references" />

### 1.3 References

|                          |                                                                                                                                                                           |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hillel auto - QA project | [Hillel QAuto - working version](https://qauto.forstudy.space/)                                                                                                           |
| Hillel auto - QA project | [Hillel QAuto - version with bugs](https://qauto2.forstudy.space/)                                                                                                        |
| Application design       | [Hillel QAuto - app design](https://www.figma.com/proto/Wy5XbgpfZpu9SasJO2QhnO/Hillel-Auto-1.2?node-id=52482-621&viewport=697%2C46%2C0.5580483675003052&scaling=min-zoom) |
| Project specification    | [Hillel QAuto - specification]( https://confluence.ithillel.com/pages/viewpage.action?spaceKey=HA&title=Hillel+auto)                                                      |
| API Documentation        | [Hillel QAuto - api-docs](https://qauto.forstudy.space/api-docs/)                                                                                                         |


---
<a name="preconditions" />

### 2. Preconditions

To effectively test the login pop-up on the website [Hillel QAuto](https://qauto.forstudy.space/)  following preconditions must be met:

1. Account Creation: An existing account must be created on the website with valid credentials, including a username, email address, and password.

2. Active Account: The account created must be active and not suspended or disabled.

3. Credentials: Valid login credentials, including the username or email address and associated password, should be noted down for successful login attempts.

4. Compatibility: The testing environment, including the browser, operating system, and device, must be compatible with the website to access the login pop-up without any compatibility issues.

5. Stable Internet Connection: A stable and reliable internet connection is required throughout the testing process to ensure successful login attempts and communication with the website's server.

6. Pop-up Functionality: The website's login pop-up must be functioning correctly and visible on the screen when the designated login button or link is clicked.

7. Clear Cache and Cookies: Any cached data or cookies associated with the website or previous login attempts must be cleared to start the test plan with a clean slate and prevent interference or conflicts.

8. Known Issues: Awareness of any known issues or limitations related to the login pop-up functionality on the website is necessary to address specific areas of concern or potential pitfalls.

9. Selenium Setup: Selenium WebDriver must be set up correctly in the Python environment, including installing the necessary packages and dependencies.

10. WebDriver Configuration: The Selenium WebDriver should be properly configured to work with the chosen browser, including setting up the driver executable and specifying the browser type and version.

11. Test Environment: The test environment, created in PyCharm or the preferred IDE, must be properly set up, including the project setup, Python interpreter selection, and installation of any additional libraries or packages required for the testing framework.

12. Test Framework: A suitable test framework, such as unittest or pytest, must be chosen and configured within the test environment to structure and organize the test cases effectively.

13. Test Script: A Python test script should be created using PyCharm or the chosen IDE, containing the necessary code to interact with the login pop-up, input valid credentials, and verify the expected behavior.

14. Test Data: The required test data, including the valid username or email address and associated password, must be prepared and made available for the test script. This data can be stored in variables or fetched from external sources like CSV files or databases.

15. Test Dependencies: Any external dependencies or resources required by the test script, such as browser drivers or additional libraries, must be properly installed and configured to avoid compatibility issues.

16. Logging and Reporting: Logging and reporting mechanisms should be set up to capture relevant test information, such as successful logins, failed attempts, error messages, or any other important details, for effective troubleshooting and analysis of the test results.

17. Test Execution Environment: The target website [Hillel QAuto](https://qauto.forstudy.space/) must be accessible and available during the test execution, and any necessary test accounts or test data on the website should be in the expected state.<br/>
By ensuring these preconditions are met, you can proceed with developing and executing your  test script using preferred IDE and preferred program language for testing the login pop-up on the website.
---
<a name="test_strategy" />

### 3. Test strategy
* **Testing Login Pop-up:**  
When testing a login pop-up, the primary goal is to ensure that the user authentication process functions correctly and securely. The testing process involves verifying the behavior and functionality of the login pop-up under various scenarios, ensuring that it meets the desired requirements and user expectations.

* **Automated Test Cases:**  
Automated test cases are scripts or programs that are designed to automatically execute predefined test steps and validate expected outcomes. In the context of testing a login pop-up, automated test cases can be created to simulate user interactions and validate the login functionality. These test cases cover various scenarios, including valid login credentials, invalid credentials, password resets, and account lockouts.

* **Verification Methods and Expected Results:**  
Verification methods in login pop-up testing involve comparing the actual behavior and results against the expected behavior and predefined acceptance criteria. These methods may include manual inspection, automated checks, and comparisons against documented requirements. Expected results for login pop-up testing include successful login with valid credentials, appropriate error messages for invalid credentials, successful password recovery, triggering of account lockout mechanisms, and proper validation of user input to prevent security vulnerabilities.

* **Approaches to Error Handling and Exceptional Situations:**
When dealing with error handling and exceptional situations in login pop-up testing, several approaches can be employed. These approaches focus on ensuring proper validation, informative error messages, and secure recovery mechanisms. Additionally, the login pop-up should handle system errors gracefully, log and report errors for troubleshooting purposes, and implement necessary security measures to protect against unauthorized access. <br/>
By following these approaches, the testing process aims to identify and resolve potential issues, enhance user experience, and ensure the login pop-up is secure, reliable, and provides a smooth authentication process for users.
-----
<a name="testing_objects" />

### 3.1 Testing objects

Login pop-up.

The application on the home page of the [Hillel QAuto](https://qauto.forstudy.space/)  website provides the "login pop-up". It`s a crucial component of the system that allows users to access their accounts and gain personalized access to features and information.
This modal window consists of Important elements:

- Text - ' Log in' ;
- Fields - 'Email', 'Password' ;
- Button - 'Forgot password', 'Registration', 'Login' ;
- Check-box - 'Remember me'.

-----
<a name="description_elem" />

### 3.2  Description of the testing elements according to the Project specification

|                              |             |                                                                                                                                                                 |                                                                 |
|------------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Elements                     | isMandatory | Errors                                                                                                                                                          | Description                                                     |
| Text **"Log in"**            |             |                                                                                                                                                                 |                                                                 |
| Button **Cross**             |             |                                                                                                                                                                 | Close pop up                                                    |
| Field "**Email**"            | yes         | - Empty field - "Email is required" <br/>- Wrong data - "Email is incorrect" <br/>- No user - "Wrong email or password"  <br/>- Border color red and labels red |                                                                 |
| Field "**Password**"         | yes         | - Empty field - "Password required" <br/>- No user - "Wrong email or password" <br/>- Border color red and labels red                                           |                                                                 |
| Check-box "**Remember me**"  |             |                                                                                                                                                                 | Provides more time to our cookie life                           |
| Button "**Forgot password**" |             |                                                                                                                                                                 | When the user clicks on this button shows Restore access pop up |
| Button "**Registration**"    |             |                                                                                                                                                                 | When the user clicks on this button shows Registration pop up   |
| Button "**Login**"           |             |                                                                                                                                                                 | Redirect to your profile <br/> The button is disabled if data incorrect                                 |
---
<a name="tested_features" />

### 3.3 Functionality and key features to be tested
The following is a detailed overview of the functionality and key features to be tested for the login pop-up:

1. Text "Log in":
   - This test case verifies that the login pop-up correctly displays the text "Log in." It ensures that the text is properly rendered and visible to users.


2. Button Cross:
   - The cross button serves as a close button for the login pop-up. When clicked, it should close the pop-up without performing any actions. This test case ensures that the button functions as expected and successfully closes the pop-up.
 
  
3. Field Email: <br/> The email field is used for users to enter their email addresses during the login process. Several test cases can be performed to validate its functionality:

   - Test Case 1: Empty field - This test case verifies that an error message appears stating "Email required" when the email field is left empty. It ensures that the system prompts the user to enter their email address.

   - Test Case 2: Wrong data - In this test case, an invalid email format (e.g., missing the '@' symbol) is entered. The expected result is that an error message appears stating "Email is incorrect." This test ensures that the system validates the email format correctly.

   - Test Case 3: No user - This test case verifies that an appropriate error message is displayed when an email that is not registered with the site is entered. The expected error message should state "Wrong email or password." This test ensures that the system correctly identifies unregistered email addresses.

   - Test Case 4: Border color and labels - This test case focuses on the visual representation of the email field when an error occurs. It ensures that the border color of the email field turns red and the associated labels also turn red, providing clear visual feedback to the user.
   

4. Field Password:
   - The password field is where users enter their passwords during the login process. The following test cases can be conducted to validate its functionality:

   - Test Case 1: Empty field - This test case verifies that an error message appears stating "Password required" when the password field is left empty. It ensures that the system prompts the user to enter their password.

   - Test Case 2: No user - When an incorrect password is entered for a valid email, the system should display an error message stating "Wrong email or password." This test case ensures that the system correctly identifies invalid passwords.

   - Test Case 3: Border color and labels - Similar to the email field, this test case focuses on the visual representation of the password field when an error occurs. It ensures that the border color of the password field turns red and the associated labels also turn red, providing clear visual feedback to the user.


5. Check box "Remember me":
   - The "Remember me" checkbox allows users to choose whether their login session should be remembered for future visits. This test case ensures that the checkbox retains its selection state when the login pop-up is closed and reopened. It validates that the system correctly stores and retrieves the user's preference.

Login functionality with valid credentials:
   - The test case involves entering valid email and password credentials and attempting to submit the login form. The expected result is to verify that the login is successful and the user is redirected to the appropriate page or dashboard. This test ensures that the login process functions as intended for users with valid credentials.

-----
<a name="checklist" />

### 3.4 Checklist and Test Cases for Login Pop-up 

This checklist appears to be a set of test cases or steps for testing the functionality and behavior of a login pop-up or form on a website or application. Each test case describes an action, the expected result, and whether the state (pass or no) matches the expected result.<br/>
The checklist covers various scenarios related to the login functionality, such as verifying the display of text, closing the login pop-up, validating the email and password fields, handling error messages, and checking the behavior of the "Remember me" checkbox.<br/>
The purpose of this checklist is to ensure that the login feature functions correctly and meets the expected requirements. By performing these tests, one can identify any issues or bugs in the login functionality and take appropriate actions to fix them before releasing the website or application to users.

#### Negative Login Functionality Test Cases

|                         |                                                                                                                                |                                                                                                                   |                |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------| -------------- |
| Elements                | Action                                                                                                                         | Expected Result                                                                                                   | State(pass/no) |
| Text "Log in"           | <a name="n1_1" /> [n1_1](#n1_1) Compare the retrieved text value with the expected text "Log in" to ensure it matches exactly. | The retrieved text value "Log in" matches the expected text "Log in" exactly, indicating that the text is displayed correctly.                                                | yes            |
| Button Cross            | <a name="n2_1" /> [n2_1](#n2_1) Click on the cross button and ensure that the login pop up is closed.                          | Closing the Log in window.                                                                                        | yes            |
| Field Email             | <a name="n3_1" /> [n3_1](#n3_1) Leave the email field empty and attempt to submit.                                             | Verify that an error message appears stating "Email required."                                                    | yes            |
|                         | <a name="n3_2" /> [n3_2](#n3_2) Enter an invalid email format (without '@' symbol) and attempt to submit.                      | Verify that an error message appears stating "Email is incorrect."                                                | yes            |
|                         | <a name="n3_3" /> [n3_3](#n3_3) Enter an email that is not registered with the site and attempt to submit.                     | Verify that an error message appears stating "Wrong email or password."                                           | yes            |
|                         | <a name="n3_4" /> [n3_4](#n3_4) Verify the visual representation of the email field when an error occurs.                      | Verify that the border color of the email field turns red, and labels associated with the field also turn red.    | yes            |
| Field Password          | <a name="n4_1" /> [n4_1](#n4_1) Leave the password field empty and attempt to submit.                                          | Verify that an error message appears stating "Password required."                                                 | yes            |
|                         | <a name="n4_2" /> [n4_2](#n4_2) Enter an incorrect password for a valid email and attempt to submit.                           | Verify that an error message appears stating "Wrong email or password."                                           | yes            |
|                         | <a name="n4_3" /> [n4_3](#n4_3) Verify the visual representation of the password field when an error occurs.                   | Verify that the border color of the password field turns red, and labels associated with the field also turn red. | yes            |
| Check-box "Remember me" | <a name="n5_1" /> [n5_1](#n5_1) Check the "Remember me" check-box                                                              | Verify that it retains the selection state when the login pop up is closed and reopened.                          | yes            |

#### Login functionality with valid credentials


|                          |                                                                                                                                                                          |                                                                                                                    |                |
| ------------------------ |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------ | -------------- |
| Elements                 | Action                                                                                                                                                                   | Expected Result                                                                                                    | State(pass/no) |
| Valid Email and Password | <a name="p5_1" /> [p1_1](#p5_1) Enter a valid email and password combination and attempt to submit.                                                                      | Verify that the login is successful and the user is redirected to the appropriate page or dashboard.               | yes            |
| Case Sensitivity         | <a name="p5_2" /> [p1_2](#p5_2) Enter the email and password combination with different case sensitivity (e.g., uppercase, lowercase, mixed case) and attempt to submit. | Verify that the login is case-insensitive and the user is able to log in successfully regardless of the case used. | yes            |
</details>

---
<a name="environment" />

### 4. Test Environment

|                                              |                                                                                                                                          |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Hardware/software configuration              | - Hardware configuration: Intel Core i7-8700K CPU, 31GB RAM, 232.89 SSD<br/> - Software configuration:  x86_64 GNU/Linux/Debian 6.1.15-1 |
| Environment settings                         | - Browser: Firefox Nightly 117.9a1 (64-bit) <br/> - Screen resolutions: 2560x1440                                                        |
| Documentation tools used                     | - KDE - KWrite <br/> - Obsidian v1.3.5                                                                                                   |
| Automation tools used                        | - PyCharm 2023.1.3 (Community Edition) <br/> - Program language - Python 3.11 <br/> - Selenium web driver                                |
| Reporting and automation tools used          | - Allure 2.22.0 <br/> - GitHub Actions                                                                                                   |