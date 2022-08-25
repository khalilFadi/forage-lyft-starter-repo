from abc import ABC

from car import Car, Engine


class SternmanEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int, warning_light_on: bool):
        super().__init__(last_service_mileage, current_mileage)
