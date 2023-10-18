from abc import ABC, abstractmethod

class TireService(ABC):
    @abstractmethod
    def needs_service(self, tire_wear):
        pass
