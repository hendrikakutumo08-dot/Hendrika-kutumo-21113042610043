languages = ["python", "java", "c++", "javascript", "C++", "Ruby"]

languages.append("Go")
languages.insert(2, "Rust")
del languages[0]
popped_lang = languages.pop(3)

print(f"List setelah dimodifikasi: {languages}")
print(f"Bahasa yang di-pop adalah: {popped_lang}")
print(f"diurutkan sementara (A-Z) {sorted(languages)}")
print(f"Total bahasa di dalam list saat ini: {len(languages)}")