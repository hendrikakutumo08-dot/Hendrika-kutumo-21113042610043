usernames = ['budi', 'siti', 'admin', 'joko', 'dewi']
for user in usernames:
    if user == 'admin':
        print("halo admin, apakah Anda ingin melihat status hari ini?")
    else:
        print(f"halo {user.title()}, terima kasih telah masuk kembali.")
print("\n")