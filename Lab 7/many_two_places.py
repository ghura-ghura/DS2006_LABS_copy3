visited_places = {
"city": "",
"country": "",
"dates": [],
}
my_visited_places = []
for i in range(0, 2):
    # Make a copy of the dictionary template:
    places = visited_places.copy()
    places["city"] = input("Enter city name: ")
    places["country"] = input("Enter country name: ")
    times = input("How many times you visited?")
    for j in range(0, int(times)):
        year = input(f"Enter the year of the {j+1} time you went there: ")
        places["dates"].append(year)
    my_visited_places.append(places)
print(my_visited_places)

# Output:
"""
Enter city name: Trollhättan
Enter country name: Sweden
How many times you visited?6 
Enter the year of the 1 time you went there: 2023
Enter the year of the 2 time you went there: 2023
Enter the year of the 3 time you went there: 2024
Enter the year of the 4 time you went there: 2024
Enter the year of the 5 time you went there: 2024
Enter the year of the 6 time you went there: 2024
Enter city name: Borås
Enter country name: Sweden
How many times you visited?2
Enter the year of the 1 time you went there: 2024
Enter the year of the 2 time you went there: 2024
[
    {'city': 'Trollhättan', 'country': 'Sweden','dates': ['2023', '2023', '2024', '2024', '2024', '2024', '2024', '2024']},
    {'city': 'Borås', 'country': 'Sweden', 'dates': ['2023', '2023', '2024', '2024', '2024', '2024', '2024', '2024']}
]
"""