from datetime import date, datetime
from re import S
from car import Car, Battery, Engine

NubbinBattery = Battery(max_years = 4)
SpindlerBattery = Battery(max_years = 2)


CapuletEngine = Engine(30000)
SternmanEngine = Engine(0) #works on light warning 
WilloughbyEngine = Engine(60000)

def create_calloiope():
    return Car(CapuletEngine, SpindlerBattery)

def create_glissade():
    return Car(WilloughbyEngine, SpindlerBattery)

def create_palindrome():
    return Car(SternmanEngine, SpindlerBattery)

def create_rorschach():
    return Car(WilloughbyEngine, NubbinBattery)

def create_thovex():
    return Car(CapuletEngine, NubbinBattery)

