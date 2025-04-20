
import datetime    # from datetime 

class Notification:
    def __init__(self, message: str, recipient: str, notification_type: str):
        self.message = message
        self.recipient = recipient                  # Could be an email or phone number
        self.notification_type = notification_type  # examp "Reminder", "Confirmation"
        self.timestamp = datetime.now()

    def send(self):
        print(f"[{self.timestamp}] Sending {self.notification_type} to {self.recipient}: {self.message}")

    def schedule_reminder(self, delay_minutes: int):
        print(f"Scheduled a reminder for {self.recipient} in {delay_minutes} minutes.")
