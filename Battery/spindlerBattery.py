from datetime import datetime
from abc import ABC
from car import Car

class SpindlerBattery(Car, ABC):
    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            eturn True
        else:
            return False
    

