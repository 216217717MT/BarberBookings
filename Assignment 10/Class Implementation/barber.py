
class Barber:
    def __init__(self, barber_id, name, specialty, availability_schedule=None):
        self._barber_id = barber_id
        self._name = name
        self._specialty = specialty
        self._availability_schedule = availability_schedule or []

    def get_barber_id(self):
        return self._barber_id

    def get_name(self):
        return self._name

    def get_specialty(self):
        return self._specialty

    def get_availability(self):
        return self._availability_schedule

    def add_availability(self, schedule_item):
        self._availability_schedule.append(schedule_item)

    def remove_availability(self, schedule_item):
        if schedule_item in self._availability_schedule:
            self._availability_schedule.remove(schedule_item)

    def __str__(self):
        return f"Barber(ID: {self._barber_id}, Name: {self._name}, Specialty: {self._specialty})"

