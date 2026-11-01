places = ["Jepang", "Raja Ampat", "Singapura", "Malaysia", "Thailand"]

print("1. List asli:", places)
print("2. Urutan alfabet sementara:", sorted(places))
print("3. Memastikan list asli tidak berubah:", places)
print("4. Urutan alfabet terbalik sementara:", sorted(places, reverse=True))
print("5. Memastikan list asli tetap tidak berubah:", places)

places.reverse()
print("6. List setelah di balik urutannya:", places)

places.reverse()
print("7. List kembali ke urutan semula:", places)

places.sort()
print("8. List diurutkan secara permanen ( A-Z):", places)

places.sort(reverse=True)
print("9. List diurutkan secara permanen ( Z-A):", places)  