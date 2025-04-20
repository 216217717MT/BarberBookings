
class Payment:
    def __init__(self, payment_id: str, appointment, amount: float, method: str, status: str = "Pending"):
        self._payment_id = payment_id
        self._appointment = appointment
        self._amount = amount
        self._method = method                    # examp "Card", "Cash", "Online"
        self._status = status

    def complete_payment(self):
        self._status = "Completed"

    def fail_payment(self):
        self._status = "Failed"

    def get_status(self):
        return self._status

    def get_payment_details(self):
        return {
            "payment_id": self._payment_id,
            "appointment": self._appointment,
            "amount": self._amount,
            "method": self._method,
            "status": self._status
        }
