#helps in declared methods that are not called
from car import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        super().__init__(last_service_mileage, current_mileage)
    
    def needs_service(self, max_mileage = 3000):
        return super.needs_service(max_mileage)