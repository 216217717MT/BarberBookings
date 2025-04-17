# A /src directory with all class implementations
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def book_appointment(self, appointment):
        pass

    def view_history(self):
        pass


class Barber:
    def __init__(self, barber_id, name, specialty):
        self.barber_id = barber_id
        self.name = name
        self.specialty = specialty

    def update_schedule(self, schedule):
        pass


class Schedule:
    def __init__(self, schedule_id, barber_id, available_slots):
        self.schedule_id = schedule_id
        self.barber_id = barber_id
        self.available_slots = available_slots

    def add_slot(self, slot):
        pass

    def remove_slot(self, slot):
        pass


class Appointment:
    def __init__(self, appointment_id, user, barber, service, time):
        self.appointment_id = appointment_id
        self.user = user
        self.barber = barber
        self.service = service
        self.time = time
        self.status = "Pending"

    def confirm(self):
        self.status = "Confirmed"

    def cancel(self):
        self.status = "Cancelled"


class Payment:
    def __init__(self, payment_id, appointment_id, amount):
        self.payment_id = payment_id
        self.appointment_id = appointment_id
        self.amount = amount
        self.status = "Unpaid"

    def process_payment(self):
        self.status = "Paid"


class Service:
    def __init__(self, service_id, name, duration, price):
        self.service_id = service_id
        self.name = name
        self.duration = duration
        self.price = price


class Admin:
    def __init__(self, admin_id, username):
        self.admin_id = admin_id
        self.username = username

    def manage_users(self):
        pass

    def manage_barbers(self):
        pass
