import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self): 
        last_service_date = date.fromisoformat("2021-03-01")
        current_date = date.fromisoformat("2024-01-27")
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2023-03-01")
        current_date = date.fromisoformat("2024-01-27")
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(battery.needs_service())