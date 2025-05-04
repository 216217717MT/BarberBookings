
# Changelog

## Assignment 12: Service Layer and REST API

### Added
- Implemented **Service Layer** for core business logic:
  - `UserService` for user operations.
  - `BarberService` for barber operations.
  - `AppointmentService` for appointment scheduling and management.

- Developed **REST API Endpoints** using FastAPI:
  - CRUD endpoints for Users, Barbers, and Appointments.
  - Business rule validations with appropriate error responses.

- Enabled **API Documentation**:
  - manually-generated OpenAPI (Swagger UI) at `/docs`. however did not work out
  - Includes endpoint details, response models, and status codes.

- Wrote **Integration Tests** using `TestClient` from FastAPI:
  - Verified create, read, update, and delete operations for all main entities.
  - Tests grouped in `/tests/integration` directory.

### Fixed
- Proper exception handling for cases like resource not found, duplicates, and validation.

### Notes
- Services are wired with **in-memory repositories** (Assignment 11).
- Repository instantiation is abstracted using the **Factory Pattern** (Assignment 10).
- All routes tested for basic HTTP correctness.
- Swagger UI screenshot available in `/docs`.
- Screenshot of my GitHub Project Board showing completed tasks

---

