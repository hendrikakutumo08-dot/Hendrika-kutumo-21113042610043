hewan_1 = {'jenis': 'kucing', 'pemilik': 'budi'}
hewan_2 = {'jenis': 'anjing', 'pemilik': 'siti'}
hewan_3 = {'jenis': 'kelinci', 'pemilik': 'agus'}

pets = [hewan_1, hewan_2, hewan_3]

print("--- Daftar Hewan Peliharaan ---")
for pet in pets:
    print(f"Jenis hewan: {pet['jenis'].title()}")
    print(f"Nama pemilik: {pet['pemilik'].title()}\n")