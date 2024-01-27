import unittest

from tire.octoprime import Octoprime;

class Octoprime(unittest.TestCase):
    def test_needs_service_true(self):
        wear_sensors = [1, 1, 1, 0.3]
        tire = Octoprime(wear_sensors=wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear_sensors = [0.1, 0.4, 0.3, 0.8]
        tire = Octoprime(wear_sensors=wear_sensors)
        self.assertFalse(tire.needs_service())       

