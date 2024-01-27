from tire.tire import Tire

class Carrigan(Tire):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors
    
    def needs_service(self):
        wheels_wear = 0
        for wear in self.wear_sensors:
            if wear >= 0.9:
                wheels_wear += 1

        return wheels_wear >= 1
