
**Reflection on Translating Requirements into Use Cases and Test Cases**

**Understanding Stakeholder's Needs**

One of the biggest challenges in this assignment was ensuring that stakeholder requirements were correctly mapped into functional use cases and test cases. The Online Booking System for Barbershops has multiple user roles, clients, barbers, and administrators, each with varying needs. It was essential to comprehend how these roles interact with the system through a detailed analysis of the functional requirements outlined in Assignment 4. For example, barbers needed a way to manage their calendars, while customers needed an easy-to-use interface to schedule and modify appointments. Ensuring that such interactions were well-defined in the use cases helped bridge the gap between system functionality and stakeholder expectations.

**Use Case Modeling Challenges**

Creating the use case diagram was also difficult, in the sense that it required a clear differentiation between different actors and their actions. Some use Cases, such as "Booking an Appointment," were reliant on others, like "Checking Barber Availability" and "Processing Payment." It required thought to know when to use inclusion (e.g., booking confirmation relies on successful payment) and when to use extension (e.g., appointment reminders as an optional extra step).
Additionally, ensuring all the functional requirements were covered in the use cases was an exhausting exercise. Some requirements, like admin functionality, were high-level and needed to be detailed in numerous sub-use cases. The use-case diagram graphically depicted these relationships and was a solid foundation for test-case development.

**Test Case Development**

Having determined the use cases, developing test cases was also challenging. One of the difficulties was testing for comprehensive test coverage of both functional and non-functional requirements.

**Functional Testing**: Ensuring that each user action led to the desired system response was critical. For instance, testing of the booking system included checking for several scenarios like successful booking, unavailable time slots, and changes in appointments.

**Edge Cases and Negative Testing**: Determining test cases that mimicked potential failures, such as attempting to update an appointment beyond the acceptable time frame, was critical in improving system reliability.

**Non-Functional Testing**: Performance and security testing required specifying measurable criteria, such as that sensitive information was protected using  encryption and page loading was under two seconds for most users. Performance testing via concurrent user simulation was difficult to execute because it required more test planning than mere functional checks

**Lessons Learned**

This project was eye-opening regarding system analysis, modeling, and verification. Some important points learned include:

**The requirement for traceability**: Ensuring that every functional requirement had been met by at least one use-case and corresponding test case.

**Real-world testing complexity**: Functional and non-functional requirements necessitate various types of testing, and some (like security testing) may need special equipment.

**Iterative refinement is necessary**: The first draft of the use case diagram and test cases often needed to be refined to reflect requirements better
