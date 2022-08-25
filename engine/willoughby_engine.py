from abc import ABC

from car import Engine


class WilloughbyEngine(Engine):
    def needs_service(self, max_mileage = 6000):
        return super.needs_service(max_mileage)
