def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profil_saya = build_profile(
    'budi', 'santoso',
    lokasi='surakarta',
    keahlian='python programming',
    hobi='membaca'
)
print(profil_saya)