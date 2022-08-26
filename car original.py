

class Car():
    def __init__(self, Engine_type, Battery_type):
        self._engine = Engine(Engine_type)
        self._battery = Battery(Battery_type)
        

    def needs_service(self):
        if(self._engine.needs_service() and self._battery.needs_service()):
            return True
        else:
            return False

class Engine():
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    def needs_service(self, max_mileage):
        return self.current_mileage - self.last_service_mileage > max_mileage

    
class Battery():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    def needs_service(self):
        pass