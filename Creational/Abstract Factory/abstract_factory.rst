Abstract Factory Pattern
========================

**Purpose**: Provide an interface for creating families of related or dependent objects without specifying their exact classes.

**When to Use**:
- When you need to create families of related objects.
- When the exact type of object that needs to be created is determined at runtime.
- When you want to enforce consistency between objects of a particular family.

**Key Characteristics**:

1. Encapsulates a group of factories (each for creating related objects).
2. Helps ensure that products from the same factory are compatible.
3. Abstracts the creation process for families of objects.

**How it Works**:

- Defines an interface (abstract factory) for creating related objects.
- Concrete factories implement the interface to create objects of specific types.
- Clients interact with the abstract factory, not the specific classes.

**Analogy**:

Imagine a furniture shop. If you're buying a "Victorian" style set, the factory gives you a Victorian-style chair, table, and sofa. For a "Modern" set, the factory provides modern furniture pieces.

**Example Use Cases**:

- Creating UI components (buttons, menus, textboxes) for different operating systems.
- Building different types of vehicles (e.g., sports cars and trucks) with their respective parts.

