class Restaurant: # Make a class called restaurant

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a beautiful restaurant, perfect for large parties")
        print(f"{self.cuisine_type} is delicious, tastey and savory.")

    def open_restaurant(self):
        print(f"Yes, {self.restaurant_name} is open!")

the_restaurant = Restaurant("Uncle Julio's", "Mexican")
print(f"My favorite restaurant is {the_restaurant.restaurant_name}")
print(f"The {the_restaurant.cuisine_type} food is yummy")
