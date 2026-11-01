guests = ["Isaac Newton", "Marie Curie", "Ada Lovelace", "Albert Einstein", "Nikola Tesla", "Elon Musk"]
print("Mohon maaf, meja baru belum datang. Kami hanya bisa mengundang 2 orang saja.\n")

popped1 = guests.pop()
print(f"Maaf {popped1}, undangan makan malam terpaksa dibatalkan.")
popped2 = guests.pop()
print(f"Maaf {popped2}, undangan makan malam terpaksa dibatalkan.")
popped3 = guests.pop() 
print(f"Maaf {popped3}, undangan makan malam terpaksa dibatalkan.")
popped4 = guests.pop()  
print(f"Maaf {popped4}, undangan makan malam terpaksa dibatalkan.\n")   

# Pesan untuk 2 orang tersisa 
print(f"\n{guests[0]}, Anda tetap di undang ke acara makan malam!")
print(f"{guests[1]}, Anda tetap di undang ke acara makan malam!")

del guests[0]
del guests[0]

print(f"\nList tamu akhir (harus kosong): {guests}")
