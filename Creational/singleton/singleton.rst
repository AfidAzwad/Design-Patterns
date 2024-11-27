Singleton Pattern
=================

**Purpose**: Ensure that a class has only one instance and provide a global access point to that instance.

**When to Use**:
- When you need a single point of control for a resource (e.g., configuration, logging, or database connections).
- When creating multiple instances might cause issues or inefficiencies.

**Key Characteristics**:

1. Only one instance of the class is created.

2. The same instance is returned every time the class is accessed.

**How it Works**:
- A private class-level variable holds the instance.
- A public method (e.g., `get_instance`) checks if the instance exists:
  - If it exists, it returns it.
  - If not, it creates and stores it.

**Analogy**:
Think of the Singleton as a radio station frequency. Once you tune in, everyone listens to the same station. No duplicate stations are created.

**Example Use Cases**:

- Logging systems (you don’t want multiple loggers writing to different files).
- Configuration managers (a central manager for app settings).
- Database connections (to manage connection pooling).
