class Car:
    def __init__(self, model, current_date, last_service_date, **kwargs):
        self.model = model
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.service_info = kwargs

    def __str__(self):
        return f"{self.model} - Last Service Date: {self.last_service_date}"