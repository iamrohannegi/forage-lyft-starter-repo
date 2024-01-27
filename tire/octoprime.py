from tire.tire import Tire

class Octoprime(Tire):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors
    
    def needs_service(self):
        total_sum = sum(self.wear_sensors)
        return total_sum >=  3
