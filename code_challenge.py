first_names = ["Mary", "Kris", "Janelle"]
last_names = ["Snow", "Bowles", "Wong"]
place = ["Maryland", "California", "New York"]
full_list = []
for i in range(3):
    bio_list = "My name is " + first_names[i] + " " + last_names[i] + " and I am from " + place[i]
    full_list.append(bio_list)
    print(full_list[i])
