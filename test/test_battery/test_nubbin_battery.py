import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self): 
        last_service_date = date.fromisoformat("2018-03-01")
        current_date = date.fromisoformat("2024-01-27")
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2022-03-01")
        current_date = date.fromisoformat("2024-01-27")
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(battery.needs_service())