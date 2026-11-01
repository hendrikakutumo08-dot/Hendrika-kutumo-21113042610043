def send_messages(messages, sent_messages):
    print("\n--- Mengirim pesan arsip ---")
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim: {current_message}")
        sent_messages.append(current_message)

daftar_pesan = ["Halo, apa kabar?", "Jangan lupa belajar Python!", "Keep coding!"]
pesan_terkirim = []

send_messages(daftar_pesan[:], pesan_terkirim)

print(f"\nDaftar pesan asli tetap utuh: {daftar_pesan}")
print(f"Daftar pesan terkirim berisi: {pesan_terkirim}")