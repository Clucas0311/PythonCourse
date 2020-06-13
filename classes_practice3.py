class User:
    active_users = 0  # class method

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1  # How to add one to class method

    def logout(self):
        User.active_users -= 1  # refer to class method and decrement it
        return f"{self.first} has logged out"

    def full_name(self):  # instance method
        return f"{self.first} {self.last}"

    def initials(self):  # instant methods
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):  # instant methods
        return f"{self.first} likes {thing}"


user1 = User("Joe", "Smith", 68)  # instances - will print
user2 = User("Blance", "Hernandez", 26)  # instances  - will print
user3 = User("Josh", "Chea", 29)  # intances  - will print

# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)
# print(user3.first, user3.last, user3.age)
print(user1.full_name())
print(user2.likes("Ice Cream"))
print(user3.likes("Chips"))

print(User.active_users)
print(user2.logout())
