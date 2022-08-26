

from configparser import MAX_INTERPOLATION_DEPTH
from locale import currency
from datetime import date, datetime
from tkinter.tix import Tree



class Car():
    #you will create car versions with each engine and battery 
    #car will have 2 variables Engine and battery
    #when needs_service() is called, functions from both engine and battery will be called
    def __init__(self, Engine_type, Battery_type, Tire_type):
        self._Engine = Engine(Engine_type)
        self._Battery = Battery(Battery_type)
        self._Tire = Tire(Tire_type)
    
    def needs_service(self, Current_date, Last_service_date, Current_mileage, last_service_mileage):
        if self._Engine.needs_service(Last_service_date , last_service_mileage, Current_mileage) or self._Battery.needs_service(Last_service_date, Current_date) or self._Tire.needs_service(self._Tire):
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

#tire function - array of 4 number between 0 and 1
class Tire():
    #2 type of tries 
    def __init__(self, tireType :str):
        #1 means will be serviced if one value is > 0.9
        #2 means will be serviced if sum of values is > 3 
        self.tireType = tireType
    #Carrigan Tires and Octoprime tires 
    #@Value has 4 inputs
    #!ADD VALUE VARIABLE HERE 
    def needs_service(self, Value):
        # if self.tireType.tireType == "carriganTires":
        #     ##!Uncomment this section to run the code accordingly (but u need to add the 4 values for each car)
        #     # for i in range(4):
        #     #     if Value[i] > 0.9:
        #     #         return True
        #     return False
        # elif self.tireType.tireType == "octoprimeTires":
        #     ##!Uncomment this section to run the code accordingly (but u need to add the 4 values for each car)
        #     # sum = 0
        #     # for i in range(4):
        #     #     sum += Value[i]
        #     # if sum > 3:
        #     #     return True
        #     return False
        return False

        #Carrigan tires should be services obly when oneor more of the values in the tire wear array is greater than or equal 0.9 
    #Octoprime tires should only be services when teh sum of all values in the tire wear array is greater than or equal 3. 
