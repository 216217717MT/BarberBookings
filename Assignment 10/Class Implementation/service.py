
class Service:
    def __init__(self, service_id: str, name: str, price: float, duration_minutes: int):
        self.service_id = service_id
        self.name = name
        self.price = price
        self.duration_minutes = duration_minutes

    def update_service_details(self, name: str = None, price: float = None, duration_minutes: int = None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if duration_minutes is not None:
            self.duration_minutes = duration_minutes

    def __str__(self):
        return f"Service({self.name}, ${self.price}, {self.duration_minutes} min)"


# Example usage (just to demonstrate correctness; will not be printed)
#example_service = Service("R50", "Haircut", 100.0)
#example_service.update_service_details(price=R150)
#example_service_str = str(example_service)
#example_service_str
