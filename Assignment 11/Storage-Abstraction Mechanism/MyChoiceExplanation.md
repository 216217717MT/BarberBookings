# The reason Why I chose Factory Pattern

I utilized the **Factory Pattern** to encapsulate the creation of the repository. This insulates the services and business logic from the storage implementation utilized. The factory produces the appropriate repository (e.g., in-memory, file, or database-backed) based on the provided storage type. This benefits flexibility, maintainability, and future-proofs the system for shifts in storage without changing the core logic.
