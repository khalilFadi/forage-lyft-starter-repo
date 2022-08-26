

from configparser import MAX_INTERPOLATION_DEPTH
from locale import currency
from datetime import date, datetime



class Car():
    #you will create car versions with each engine and battery 
    #car will have 2 variables Engine and battery
    #when needs_service() is called, functions from both engine and battery will be called
    def __init__(self, Engine_type, Battery_type):
        self._Engine = Engine(Engine_type)
        self._Battery = Battery(Battery_type)
    
    def needs_service(self, Current_date, Last_service_date, Current_mileage, last_service_mileage):
        if self._Engine.needs_service(Last_service_date , last_service_mileage, Current_mileage) or self._Battery.needs_service(Last_service_date, Current_date):
            return True
        else:
            return False

class Engine():
    def __init__(self, max_mileage :int):
        self.max_mileage = max_mileage
        pass

    def needs_service(self,last_service_date,  last_service_mileage, current_mileage):
        if type(current_mileage) == int:
            return self.based_on_mileage(last_service_date,  last_service_mileage, current_mileage)
        else:
            return self.based_on_warning_light(last_service_date,  last_service_mileage, current_mileage)

    def based_on_mileage(self, last_service_date,last_service_mileage, current_mileage):    
        return (current_mileage - last_service_mileage) > (self.max_mileage.max_mileage)

    def based_on_warning_light(self, last_service_date,last_service_mileage, warning_light_on):
        return warning_light_on
    #you will create engines with the max requriements 
    #when needs service will be called check the needed numbers 


    
class Battery():
    #when needs_service is called it will cehck the needed dates.
    def __init__(self, max_years):
        self.max_years = max_years
    
    def needs_service(self, last_service_date, current_date):
        service_threshold_date = last_service_date.replace(year = last_service_date.year + self.max_years.max_years)
        if service_threshold_date < current_date:
            return True
        else:
            return False

