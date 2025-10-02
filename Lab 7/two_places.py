visited_places = {
    "city": "",
    "country": "",
    "year": "",
}
my_visited_places = []
for i in range(0, 2):
    visited_places["city"] = input("Enter city name: ")
    visited_places["country"] = input("Enter country name: ")
    visited_places["year"] = input("Enter the year: ")
    my_visited_places.append(visited_places)
print(my_visited_places)

# Output:
# Enter city name: Trollhättan
# Enter country name: Sweden
# Enter the year: 2024
# Enter city name: Borås
# Enter country name: Sweden
# Enter the year: 2024
# [{'city': 'Borås', 'country': 'Sweden', 'year': '2024'}, {'city': 'Borås', 'country': 'Sweden', 'year': '2024'}]