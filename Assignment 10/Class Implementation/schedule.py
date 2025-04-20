# src/schedule.py

import datetime, time   # from datetime 

class Schedule:
    def __init__(self, schedule_id: str, barber, day: str, start_time: time, end_time: time):
        self._schedule_id = schedule_id
        self._barber = barber
        self._day = day                      # exp "Monday"
        self._start_time = start_time
        self._end_time = end_time

    def update_schedule(self, day: str = None, start_time: time = None, end_time: time = None):
        if day:
            self._day = day
        if start_time:
            self._start_time = start_time
        if end_time:
            self._end_time = end_time

    def is_within_schedule(self, check_time: time):
        return self._start_time <= check_time <= self._end_time

    def get_schedule_details(self):
        return {
            "schedule_id": self._schedule_id,
            "barber_id": self._barber.user_id,
            "day": self._day,
            "start_time": self._start_time.strftime("%H:%M"),
            "end_time": self._end_time.strftime("%H:%M")
        }
