angka = input("Masukkan sebuah angka, dan saya akan beri tahu jika itu kelipatan 10: ")
angka = int(angka)

if angka % 10 == 0:
    print(f"Angka {angka} adalah kelipatan 10.")
else:
    print(f"Angka {angka} bukan kelipatan 10.")