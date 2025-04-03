# Explanation of State Transition Diagrams 

# Explanation

**The following are the 7 Critical Objects with their Transitions:**

1.  **Appointment** (Booked → Confirmed → Completed → Canceled)
2.  **Payment** (Pending → Processed → Failed)
3.  **User Account** (Registered → Verified → Suspended → Deleted)
4.  **Barber Availability** (Available → Fully Booked → On Leave)
5.  **Booking Request** (Created → Pending Approval → Approved → Rejected)
6.  **Service** (Active → Inactive)
7.  **Notification** (Sent → Read)

**The following are States and Explanation**

**Appointment State**

**Explanation:** A new appointment starts as **Booked**. The barber can confirm it, moving it to **Confirmed**. If the user attends the appointment, it transitions to **Completed**. The user can also cancel it at any stage before **Completed.**

**Payment State**

**Explanation:** A payment starts as **Pending**. If successful, it moves to **Processed**; otherwise, it becomes **Failed**

**User Account State**

**Explanation:** Users register, verify their accounts, and can later be suspended or deleted.

**Barber Availability State**

**Explanation:** The barber can be **Available**, **Fully Booked**, or **On Leave**.

**Booking Request State**

**Explanation:** Booking requests go through **Pending Approval** before being either **Approved or Rejected**

**Service State**

**Explanation:** Services can be switched between **Active** and **Inactive.**

**Notification State**

**Explanation:** Notifications start as **Sent** and transition to **Read** when opened.


