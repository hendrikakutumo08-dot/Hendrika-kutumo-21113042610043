favorite_languages = {'budi': 'python', 'siti': 'c'}
daftar_target = ['budi', 'joko', 'siti', 'dewi']

for nama in daftar_target:
    if nama in favorite_languages.keys():
        print(f"Terima kasih {nama.title()} karena sudah mengisi polling!")
    else:
        print(f"Halo {nama.title()}, silahkan luangkan waktu untuk mengisi polling kami.")
print("\n")