class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


user1 = User("Joe", "Smith", 68)  # instances - will print
user2 = User("Blance", "Hernandez", 26)  # instances  - will print
user3 = User("Josh", "Chea", 29)  # intances  - will print

print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)
print(user3.first, user3.last, user3.age)
