from datetime import date, datetime
from re import S
from car import Car, Battery, Engine, Tire

NubbinBattery = Battery(max_years = 4)
SpindlerBattery = Battery(max_years = 3)


CapuletEngine = Engine(30000)
SternmanEngine = Engine(0) #works on light warning 
WilloughbyEngine = Engine(60000)

CarriganTire = Tire("carriganTires")
OctoprimTire = Tire("octoprimTires")
def create_calloiope():
    return Car(CapuletEngine, SpindlerBattery, CarriganTire)

def create_glissade():
    return Car(WilloughbyEngine, SpindlerBattery, OctoprimTire)

def create_palindrome():
    return Car(SternmanEngine, SpindlerBattery, CarriganTire)

def create_rorschach():
    return Car(WilloughbyEngine, NubbinBattery, OctoprimTire)

def create_thovex():
    return Car(CapuletEngine, NubbinBattery, OctoprimTire)

