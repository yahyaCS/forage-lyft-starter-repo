from tire_service import TireService

class CarriganTireService(TireService):
    def needs_service(self, tire_wear):
        return any(wear >= 0.9 for wear in tire_wear)