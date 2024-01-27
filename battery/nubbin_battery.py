from utils import add_years_to_date
from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service():
        date_to_service_battery = add_years_to_date(self.last_service_date, 4)
        if date_to_service_battery < self.current_date:
            return True
        else:
            return False