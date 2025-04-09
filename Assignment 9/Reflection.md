
**Reflection**

It was an enriching and educational experience to create the class diagram and domain model for my **System**. It helped me better appreciate how the concepts of **Object-Oriented Design (OOD)** can be applied to represent the real-world problems in a software system. Although I had previously done requirements, use cases, and behavior models, this phase required a mindset shift focusing more on the system's static structure and logic rather than on the user flows or interfaces.

**Challenges Encountered**

One of the biggest challenges I faced was trying to decide how to abstract each class should be. It was difficult initially to know what a class should be and what could be done as an attribute or method. For example, whether **Schedule** should be an entity on its own or be an attribute of Barber was something I had to think very carefully about how it would function in the system. Similarly, describing the **admin** role with responsibilities like dealing with **users** and **barbers** needs balance between simplicity and completeness.

Establishing explicit relationships between entities, specifically when adding multiplicity, was another challenge. Ensuring relationships such as "A **barber** can have many appointments, but each appointment can have one **barber**" or "**Users**(clients) can have many appointments but not at the same time" involved revisiting previous diagrams and solidifying the business logic. Method definition was also a difficult area. I wanted to populate classes with methods for every possible action but had to focus on basic responsibilities in accordance with the primary use cases of the system. Getting these methods to be cohesive and representative of the class's responsibility was a learning experience.

**Alignment with Previous Assignments**

The class diagram closely corresponds to the use cases defined in **Assignment 5**, especially the use cases for booking management, user registration, and payment processing. For example, the Appointment class can easily support the "Book Appointment" use case, and the Payment class corresponds to "Process Payment."

From **Assignment 4** (Functional Requirements), many of the features like appointment modification, user management, and admin controls are clearly represented in the model. The behavior modeled in state and activity diagrams from **Assignment 8** is also reflected, here is an example, appointment modification lifecycle state transitions such as "Pending → Confirmed → Completed" simply become states which appointments can be in, again ensuring continuity throughout all design documents.

**Trade-Offs Made**

One of the significant trading-offs was maintaining the use of inheritance straightforward. Even though having **Admin**, **Barber**, and **Client** as subclasses of **User** would have been nice, I avoided making them full-fledged subclasses since I maintained them as distinct roles with possibly shared attributes, rather than being subclasses. This simplified diagram complexity allowed me to focus on what mattered, instead of creating a sophisticated hierarchy that might or might not be heavily utilized within the context of the current system. Likewise, I did not overly complicate the **Schedule** class with time slot inheritance or composition to simplify things. The trade-offs made were to have clear diagrams and keep the prime system features highlighted.

**Lessons Learned**

This exercise enhanced my knowledge of domain modeling and object-oriented analysis. I came to appreciate how crucial it is to map business logic to design elements clearly and how good modeling aids implementation planning. It also emphasized the importance of consistency following ideas from requirements to diagrams ensures that no important feature gets lost in translation. Most importantly, I’ve gained confidence in designing scalable, maintainable systems using structured design principles. These diagrams will serve as a blueprint for actual implementation and provide communication clarity between stakeholders and developers.
