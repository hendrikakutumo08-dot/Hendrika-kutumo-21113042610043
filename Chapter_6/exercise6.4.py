glossary = {
    'string': 'Kumpulan karakter berupa teks.',
    'list': 'Kumpulan item yang di simpan dengan urutan tertentu.',
    'dictionary': 'Kumpulan pasangan kunci (key) dan nilai (value).',
    'loop': 'menjalankan blok kode secara berulang.',
    'key': 'identitas unik penunjuk nilai di dalam dictionary.'
}
for kata, definisi in glossary.items():
    print(f"{kata.title()}: {definisi}")
print("\n")