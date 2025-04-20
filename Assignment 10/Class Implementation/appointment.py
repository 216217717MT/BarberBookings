

import datetime  # from datetime 

class Appointment:
    def __init__(self, appointment_id: str, client, barber, schedule, time: datetime, status: str = "Pending"):
        self._appointment_id = appointment_id
        self._client = client
        self._barber = barber
        self._schedule = schedule
        self._time = time
        self._status = status

    def confirm(self):
        self._status = "Confirmed"

    def cancel(self):
        self._status = "Canceled"

    def get_status(self):
        return self._status

    def get_details(self):
        return {
            "appointment_id": self._appointment_id,
            "client": self._client,
            "barber": self._barber,
            "schedule": self._schedule,
            "time": self._time,
            "status": self._status
        }
