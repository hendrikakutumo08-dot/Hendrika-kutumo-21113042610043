def make_sandwich(*ingredients):
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('daging sapi', 'keju')
make_sandwich('ayam', 'selada', 'tomat')
make_sandwich('telur', 'mayones', 'sosis', 'bombay')