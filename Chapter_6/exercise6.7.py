person1 = {
    "first_name": "Budi",
    "last_name": "Santoso",
    "age": 20,
    "city": "Solo"
}

person2 = {
    "first_name": "Siti",
    "last_name": "Aminah",
    "age": 19,
    "city": "Semarang"
}

person3 = {
    "first_name": "Andi",
    "last_name": "Pratama",
    "age": 21,
    "city": "Yogyakarta"
}

people = [person1, person2, person3]

for person in people:
    print("\nInformasi orang:")

    for key, value in person.items():
        print(key.replace("_", " ").title() + ":", value)