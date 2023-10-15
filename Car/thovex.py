import nubbinBattery
from datetime import datetime
from engine.capulet_engine import CapuletEngin

class Thovex(CapuletEngine):
   def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
