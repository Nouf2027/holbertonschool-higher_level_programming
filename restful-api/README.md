# HBnB Evolution — UML & Technical Documentation

## Project Overview

This project focuses on designing and documenting the architecture of the **HBnB Evolution** system.
It emphasizes UML modeling, architectural design, and API interaction flows to provide a clear
technical blueprint that guides future implementation phases.

The documentation covers system structure, business logic design, and request flows without
including implementation details or source code.

---

## Learning Objectives

- Understand layered architecture design
- Apply UML diagrams to model system structure and behavior
- Design Business Logic using clear domain entities
- Illustrate API interaction flows using sequence diagrams
- Apply the Facade design pattern
- Produce professional technical documentation

---

## Documentation Scope

This technical document includes:

- High-Level Package Diagram
- Detailed Class Diagram for the Business Logic Layer
- Sequence Diagrams for core API interactions
- Explanatory notes describing design decisions and system flow

---

## Tasks

| Task | Description | File |
|-----:|------------|------|
| 0 | High-Level Package Diagram | `High-Level-Package-Diagram.png` |
| 1 | Business Logic Class Diagram | `Detailed-Class-Diagram.png` |
| 2 | User Registration Sequence Diagram | `user_registration.png` |
| 3 | Place Creation Sequence Diagram | `place_creation.png` |
| 4 | Review Submission Sequence Diagram | `review_submission.png` |
| 5 | Fetch Places Sequence Diagram | `fetch_places.png` |

---

## Architecture Overview

The system follows a layered architecture consisting of:

- **Presentation Layer:** Handles API requests and responses.
- **Business Logic Layer:** Contains core entities, rules, and workflows.
- **Persistence Layer:** Manages data storage and retrieval.

A **Facade** is used to mediate communication between the Presentation and Business Logic layers,
ensuring loose coupling and maintainability.

---

## Author

- **Name:** Nouf Almutairi
- **GitHub:** @Nouf2027
