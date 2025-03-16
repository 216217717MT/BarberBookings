
**Use Case Specifications**

**Book an Appointment**

**Actor**: Customer

**Description**: Allows the customer to select a barber, select a service, and select an available time slot to book an appointment.

**Preconditions**: The customer must be logged into the system.

**Postconditions**: The appointment is booked, and the system informs the customer with a confirmation message.

**Basic Flow**:

1. Customer selects a barber from the list.

2. Customer selects a service from the available services list.

3. The system shows available time slots for the selected barber.

4. The customer selects a time slot.

5. The system confirms the appointment and sends an SMS and email confirmation to the customer.

**Alternative Flows**:

If there are no available time slots, the system flashes a message requesting the customer to choose a different time.

If the selected barber is unavailable, the system requests the customer to choose another barber

**Modifying Appointment**

**Actor**: Customer

**Description**: Allows the customer to edit or cancel an already scheduled appointment.

**Preconditions**: The customer has logged in and has a confirmed appointment.

**Postconditions**: The appointment has been edited or canceled, and the customer has displayed the new confirmation.

**Basic Flow**:

1. Customer logs into the system.

2. Customer views his or her future appointments.

3. Customer selects the appointment he or she wishes to edit or cancel.

4. Customer edits the appointment details or cancels.

5. The system sends new confirmation via SMS and email.

**Alternative Flows**:

If the change is done within 24 hours of the appointment, the system can prevent the changes.

If the appointment is canceled, the system cancels it from the customer's calendar.

**View Booking History**

**Actor**: Customer

**Description**: Allows the customer to view their past, upcoming, and canceled appointments.

**Preconditions**: The customer must be logged in.

**Postconditions**: The system displays the customer's booking history with sorted controls.

**Basic Flow**:

1. Customer logs into the system.

2. Customer selects the "Booking History" option.

3. The system displays a list of past and upcoming appointments.

4. The customer can filter and sort history by appointment status.

**Alternative Flows**: In case there are no bookings, the system will show a message that there are no appointments available

**View Real-Time Availability**

**Actor**: Barber, Customer

**Description**: The system checks and displays the real-time availability of barbers.

**Preconditions**: The barber must already have set their working hours, and the customer is searching for available slots.

**Postconditions**: The system displays available time slots for booking.

**Basic Flow**:

1.The customer selects a barber.

2.The system checks the barber's schedule for available time slots.

3.The available time slots are displayed for the customer to choose.

**Alternative Flows**: If slots are not available, the system requests the customer to choose an alternative barber or time

**Process Payment**

**Actor**: Payment Gateway, Customer

**Description**: The system processes payment for a customer's appointment via an online payment gateway.

**Preconditions**: The customer must have a confirmed appointment.

**Postconditions**: The payment is processed successfully, and the customer receives a payment receipt.

**Basic Flow**:

1.Customer selects a payment option.

2.The system redirects the customer to the payment gateway.

3.Customer enters payment details and confirms the payment.

4.The payment gateway processes the payment.

5.The system processes payment and sends a receipt to the customer via email.

**Alternative Flows**: If payment fails, the system displays an error message, and the customer is prompted to retry.

**Send Appointment Reminder**

**Actor**: System, SMS/Email System

**Description**: Sends an automatic reminder to the customer 24 hours before their appointment.

**Preconditions**: The customer must have a confirmed appointment.

**Postconditions**: The customer receives an appointment reminder via SMS and email.

**Basic Flow**:

1.The system checks the upcoming appointments for the next 24 hours.

2.The system sends the customer an appointment reminder.

**Alternative Flows**: the customer has already modified or canceled the appointment, no reminder is sent

**Admin Dashboard**

**Actor**: Admin

**Description**: Admin manages barbers, appointments, and client feedback through dashboard interface.

**Preconditions**: Admin must be logged into the system.

**Postconditions**: Admin has added barbers, appointments, or client feedback as required.

**Basic Flow:**

1.Admin logs into the system.

2.Admin looks at the dashboard.

3.Admin can view all appointments and client feedback.

4.Admin updates barbers' schedules and assign services.

**Alternative Flows:** There are no appointments, the system shows a "No Appointments" message.

**Update Client Profile**

**Actor**: Customer

**Description**: The customer can update their personal information and see their previous appointments.

**Preconditions**: The customer is logged into the system.

**Postconditions**: The customer's profile is updated with the new information.

**Basic Flow**:

1.Customer logs into their profile.

2.Customer chooses the option to update profile information.

3.Customer updates contact details or other appropriate information.

4.The system saves the updated profile.

**Alternative Flows**: If the customer fails to save the updated details, the system prompts them to retry.
