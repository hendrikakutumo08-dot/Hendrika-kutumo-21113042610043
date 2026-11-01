sandwich_orders = ['tuna', 'turkey', 'grilled cheese', 'chicken bacon']
finished_sandwiches = []

while sandwich_orders:
    sandwich_sekarang = sandwich_orders.pop()
    print(f"Saya telah membuat sandwich {sandwich_sekarang} Anda.")
    finished_sandwiches.append(sandwich_sekarang)

print("\n--- Semua sandwich telah selesai dibuat ---")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich.title()}")