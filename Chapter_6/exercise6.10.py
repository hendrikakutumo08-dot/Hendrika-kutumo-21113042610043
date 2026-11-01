favorite_numbers = {
    "Budi": [7, 10, 25],
    "Siti": [3, 8],
    "Andi": [12, 15, 20],
    "Rina": [4, 9],
    "Doni": [6, 11, 30]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print()