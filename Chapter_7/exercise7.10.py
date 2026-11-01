hasil_survei = {}
polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa nama Anda? ")
    jawaban = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")

    hasil_survei[nama] = jawaban
    
    ulangi = input("Apakah ada orang lain yang ingin menjawab? (yes/no) ")
    if ulangi.lower() == 'no':
        polling_aktif = False

print("\n--- Hasil Survei Liburan Impian ---")
for nama, tempat in hasil_survei.items():
    print(f"{nama.title()} ingin pergi berlibur ke {tempat.title()}.")