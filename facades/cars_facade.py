import allure
from models.cars import Cars, Car, CarData


class CarsFacade(Cars):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Retrieve cars via API")
    def get(self) -> list[Car]:
        return super().get()

    @allure.step("Create car via API")
    def create(self, data: CarData) -> Car:
        return super().create(data)

    @allure.step("Delete cars via API")
    def delete_cars(self, cars: list[Car]):
        return super().delete_cars(cars)

    @allure.step("Delete ALL cars via API")
    def delete_all_cars(self):
        return super().delete_all_cars()
