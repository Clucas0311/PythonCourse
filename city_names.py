# Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string
# formatted like this "Santiago, Chile"

def city_country(city, country):
    full_country = f"{city}, {country}"
    return full_country

country = city_country("Olney", "USA")
print(country)
