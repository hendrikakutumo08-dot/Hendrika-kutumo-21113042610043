def make_album(artist_name, album_title):
    return {'artist': artist_name.title(), 'title': album_title.title()}

while True:
    print("\n--- Masukkan informasi album ---")
    print("(Ketik 'q' kapan saja untuk keluar)")
    
    artis = input("Nama Artis: ")
    if artis == 'q':
        break
        
    judul = input("Judul Album: ")
    if judul == 'q':
        break
        
    album_user = make_album(artis, judul)
    print(f"Hasil pembuatan album: {album_user}")