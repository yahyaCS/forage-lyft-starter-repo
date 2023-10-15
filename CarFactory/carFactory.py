import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car("Calliope", current_date, last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car("Glissade", current_date, last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car("Palindrome", current_date, last_service_date, warning_light_on=warning_light_on)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car("Rorschach", current_date, last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car("Thovex", current_date, last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)