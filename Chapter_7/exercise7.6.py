perintah = "\nMasukkan usia Anda untuk mengecek harga tiket:"
perintah += "\n(Ketik 'quit' untuk keluar): "

active = True
while active:
    input_usia = input(perintah)
    
    if input_usia == 'quit':
        active = False
    else:
        usia = int(input_usia)
        if usia < 3:
            print("  Tiket Anda gratis!")
        elif usia <= 12:
            print("  Harga tiket Anda adalah $10.")
        else:
            print("  Harga tiket Anda adalah $15.")