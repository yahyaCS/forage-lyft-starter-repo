from tire_service import TireService

class OctoprimeTireService(TireService):
    def needs_service(self, tire_wear):
        return sum(tire_wear) >= 3