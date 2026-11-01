# Mengembangkan data Latihan 6-1 (Person) dengan menambah data hobi (bentuk list) di dalamnya
person = {
    'first_name': 'rizky',
    'last_name': 'hidayat',
    'age': 22,
    'city': 'surakarta',
    'hobi': ['membaca', 'berenang', 'koding'] # Fitur tambahan baru pengembangan
}
print(f"Profil Lengkap {person['first_name'].title()} {person['last_name'].title()}:")
print(f"- Kota tinggal: {person['city'].title()}")
print(f"- Usia: {person['age']} tahun")
print("- Daftar hobi saat ini:")
for hobi in person['hobi']:
    print(f"  * {hobi}")