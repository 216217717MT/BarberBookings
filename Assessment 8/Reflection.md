# Reflection

# Reflection

**Challenges in Choosing Granularity for States & Actions**

One of the biggest challenges was determining the right level of detail for both state transition diagrams and activity workflow diagrams. If the diagrams were complex, they became cluttered and difficult to follow. If they were too high-level, they lacked clarity for developers and stakeholders. For example, In the Appointment Booking State Diagram, I had to decide whether I should draw microstates like "Payment Processing" → "Payment Verified" or just a direct transition between "Pending" and "Confirmed".

**Aligning Diagrams with Agile User Stories**

Mapping state transitions and workflows to Agile user stories was crucial but tricky. Some user stories crossed multiple states and workflows. Others were contingent on multiple actors (e.g., client, barber, system). For example, the "Cancel Appointment" workflow had to support user-driven cancellations as well as automated cancellations (e.g., if a barber is unavailable). This meant ensuring that state changes (e.g., "Canceled") triggered automated refunds or rescheduling functionality.

**Comparison: State Diagrams vs. Activity Diagrams**

| Feature              | State Diagram                                      | Activity Diagram                                  |
|----------------------|---------------------------------------------------|--------------------------------------------------|
| **Focus**           | Represents the states of an object over time      | Represents the flow of activities in a process  |
| **Purpose**         | Models object behavior and transitions            | Models workflow and decision-making processes   |
| **Elements**        | States, transitions, events, and guard conditions | Start/end nodes, actions, decisions, swimlanes  |
| **Trigger**         | State changes occur due to specific events        | Activities flow based on conditions and logic   |
| **Flow Type**       | Event-driven                                       | Control flow-driven                             |
| **Use Case Example**| Order transitioning from "Pending" to "Shipped"   | Steps in a "User Registration" process         |
| **Best For**        | Object lifecycle modeling                         | Process modeling and workflow representation    |

**Lessons Learned**

I learned that **state transition diagrams** help system define logic but require careful guard conditions to avoid infinite loop traps.  While **Activity diagrams** clearly render process execution but can become complicated if two or more actors are involved (e.g., client, barber, system). Both the diagrams supplement each other such that workflows and system behaviors are suitably arranged for their implementation
