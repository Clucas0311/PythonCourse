class Dog: # defined a class called dog
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in repsonse to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6) # Create a dog whose name is Willie and is age 6
# Created and instance with the my_dog variable

# create additonal instances
your_dog = Dog("Lucy", 3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

# after we created an instance we can use the dot method to call any method defined in dog
my_dog.sit()
my_dog.roll_over()


# We can create many instances
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
