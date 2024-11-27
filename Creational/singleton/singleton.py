class Singleton:
    """A Singleton class to ensure only one instance exists."""

    _instance = None  # Class-level private variable to store the instance

    def __new__(cls, *args, **kwargs):
        # If no instance exists, create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Creating the Singleton instance.")
        else:
            print("Using the existing Singleton instance.")
        return cls._instance

    def __init__(self, value):
        """Initialize the Singleton instance with a value."""
        self.value = value


# Test the Singleton behavior
singleton1 = Singleton("First")
print(f"Singleton1 value: {singleton1.value}")

singleton2 = Singleton("Second")
print(f"Singleton2 value: {singleton2.value}")

# Verify that both references point to the same instance
print(f"Are singleton1 and singleton2 the same? {singleton1 is singleton2}")
