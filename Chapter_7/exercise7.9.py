sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'turkey', 'grilled cheese', 'pastrami']
finished_sandwiches = []

print("Mohon maaf, kedai kami kehabisan pastrami hari ini.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_sekarang = sandwich_orders.pop()
    print(f"Saya telah membuat sandwich {sandwich_sekarang} Anda.")
    finished_sandwiches.append(sandwich_sekarang)

print("\n--- Sandwich yang Selesai Dibuat ---")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich.title()}")