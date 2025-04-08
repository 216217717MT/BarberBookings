
# Domain Model Documentation


# Domain Model Table

| Entity       | Attributes                                      | Methods                                 | Relationships                                 |
|--------------|-------------------------------------------------|-----------------------------------------|-----------------------------------------------|
| User         | userId, name, email, phone, address,                    | register(), login(), updateProfile()    | Books Appointments, Makes Payments            |
| Barber       | barberId, name, specialization                  | viewSchedule(), updateAvailability()    | Handles Appointments                          |
| Appointment  | appointmentId, date, time, status               | book(), cancel(), reschedule()          | Linked to User and Barber                     |
| Service      | serviceId, name, duration, price                | addService(), updateService()           | Chosen for Appointment                        |
| Payment      | paymentId, amount, status, method               | makePayment(), refundPayment()          | Linked to User and Appointment                                              
| Notification | notificationId, message, timestamp, userId     | sendNotification()                      | Sent to User                                  |
