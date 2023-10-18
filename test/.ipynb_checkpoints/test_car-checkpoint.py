import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime, timedelta

class TestEngines(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        current_mileage = 40000
        last_service_mileage = 10000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_engine_does_not_need_service(self):
        current_mileage = 15000
        last_service_mileage = 10000
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())

    def test_sternman_engine_needs_service(self):
        warning_light_on = True
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_engine_does_not_need_service(self):
        warning_light_on = False
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertFalse(sternman_engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        current_mileage = 70000
        last_service_mileage = 50000
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service())

    def test_willoughby_engine_does_not_need_service(self):
        current_mileage = 55000
        last_service_mileage = 50000
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service())

class TestBatteries(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        current_date = datetime.now()
        last_service_date = current_date - timedelta(days=4 * 365)  # 4 years ago
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        current_date = datetime.now()
        last_service_date = current_date - timedelta(days=2 * 365)  # 2 years ago
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())

    def test_spindler_battery_needs_service(self):
        current_date = datetime.now()
        last_service_date = current_date - timedelta(days=2 * 365)  # 2 years ago
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        current_date = datetime.now()
        last_service_date = current_date - timedelta(days=1 * 365)  # 1 year ago
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())

if __name__ == '__main__':
    unittest.main()
