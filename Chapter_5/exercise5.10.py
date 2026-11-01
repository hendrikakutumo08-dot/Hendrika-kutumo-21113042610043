current_users = ['admin', 'budi', 'siti', 'joko', 'Dewi']
new_users = ['BUDI', 'jono', 'rani', 'dewi', 'ahmad']

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
       print(f"Username '{new_user}' sudah terpakai. Silahkan masukkan nama lain.")
    else:
        print(f"Username '{new_user}' masih tersedia.")
print("\n")