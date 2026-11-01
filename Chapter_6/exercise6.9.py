favorite_places = {
    'budi': ['pantai parangtritis', 'candi borobudur'],
    'siti': ['gunung merbabu'],
    'joko': ['malioboro', 'kuta bali', 'raja ampat']
}

for nama, tempat_list in favorite_places.items():
    print(f"Tempat favorit {nama.title()} adalah:")
    for tempat in tempat_list:
        print(f"  - {tempat.title()}")
    print("")