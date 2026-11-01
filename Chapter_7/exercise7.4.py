perintah = "\nMasukkan topping pizza yang Anda inginkan:"
perintah += "\n(Ketik 'quit' jika sudah selesai): "

while True:
    topping = input(perintah)
    if topping == 'quit':
        break
    else:
        print(f"  Saya akan menambahkan {topping} ke pizza Anda!")