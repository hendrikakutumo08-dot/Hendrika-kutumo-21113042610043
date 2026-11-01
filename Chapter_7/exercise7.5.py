perintah = "\nMasukkan usia Anda untuk mengecek harga tiket:"
perintah += "\n(Ketik 'quit' untuk keluar): "

while True:
    input_usia = input(perintah)
    if input_usia == 'quit':
        break
    
    usia = int(input_usia)
    if usia < 3:
        print("  Tiket Anda gratis!")
    elif usia <= 12:
        print("  Harga tiket Anda adalah $10.")
    else:
        print("  Harga tiket Anda adalah $15.")