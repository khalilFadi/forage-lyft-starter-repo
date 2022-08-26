import unittest
import carFactory
import unittest
from datetime import datetime

class TestCallope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_calloiope()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_battery_should_not_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_calloiope()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = carFactory.create_calloiope()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 3000
        last_service_mileage = 0

        car = carFactory.create_calloiope()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_glissade()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_battery_should_not_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_glissade()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = carFactory.create_glissade()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 6000
        last_service_mileage = 0

        car = carFactory.create_glissade()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_palindrome()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_battery_should_not_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_palindrome()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = True
        last_service_mileage = 0

        car = carFactory.create_palindrome()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = False
        last_service_mileage = 0

        car = carFactory.create_palindrome()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_rorschach()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_battery_should_not_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_rorschach()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = carFactory.create_rorschach()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = carFactory.create_rorschach()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_thovex()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_battery_should_not_be_serviced(self):
        #get todays date 
        today = datetime.today().date()
        #change the last service day
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = carFactory.create_thovex()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = carFactory.create_thovex()
        self.assertTrue(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = carFactory.create_thovex()
        self.assertFalse(car.needs_service(today, last_service_date, current_mileage, last_service_mileage))


if __name__ == '__main__':
    unittest.main()