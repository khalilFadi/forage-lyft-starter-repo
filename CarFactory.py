from re import S
from car import Car
from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class Engine_Creation():
    def __init__(self) -> None:
        pass

class CarFactory(Car):
    def create_calliope():
        return Car(CapuletEngine, SpindlerBattery)

    def create_glissade():
        return Car(WilloughbyEngine, SpindlerBattery)
    
    def create_palindrome():
        return Car(SternmanEngine, SpindlerBattery)

    def create_rorschach():
        return Car(WilloughbyEngine, NubbinBattery)

    def create_thovex():
        return Car(CapuletEngine, NubbinBattery)

    