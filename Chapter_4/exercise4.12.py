makanan_saya = ['nasi goreng', 'mie ayam', 'bakso']
makanan_teman = makanan_saya[:]

makanan_saya.append('sate')
makanan_teman.append('soto')

print("Makanan favorit saya adalah:")
for makanan in makanan_saya:
    print(f"- {makanan}")

print("\nMakanan favorit teman saya adalah:")
for makanan in makanan_teman:
    print(f"- {makanan}")