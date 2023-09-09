class User:
    # Class Fields (attributes) -> shared across all instances
    # No need an instance to access this can be directly accessed from the class
    default_employer = "abc"

    # Instance Fields (attributes) -> must be defined inside a constructor
    def __init__(self, name):
        self.name = name

    # Class Methods -> shared across all instances
    # No need an instance to access this can be directly accessed from the class
    @classmethod
    def get_default_employer(cls):
        return cls.default_employer

    # Instance Methods
    def say_hello(self):
        return f"Hello {self.name}!"
