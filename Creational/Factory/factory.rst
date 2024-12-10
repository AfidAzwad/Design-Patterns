Factory Pattern
===============

**Purpose**: Define an interface or method for creating objects in a super class, but allow subclasses to alter the type of objects that will be created.

**When to Use**:
- When you need to delegate the responsibility of instantiating objects to a separate class or method.
- When the exact type of object to create depends on some runtime logic.

**Key Characteristics**:
1. A factory method or class is responsible for object creation.
2. The client code does not need to know the details of the concrete class.
3. Promotes loose coupling between client code and the classes it uses.

**How it Works**:
- The factory method determines the appropriate subclass to instantiate.
- It returns an instance of the correct class based on input parameters.

**Analogy**:
Think of a pizza restaurant. When you order a pizza, you don't know or care how it's made; you just know you'll get the type of pizza you asked for.

**Example Use Cases**:
- GUI libraries where different themes (e.g., Light, Dark) create different types of buttons.
- Game development where different characters or weapons are created based on player choices.
