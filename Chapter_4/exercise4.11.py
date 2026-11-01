pizza_saya = ['pepperoni','margherita', 'bbq chicken']
pizza_teman = pizza_saya[:]
pizza_teman.append('keju ekstra')
pizza_teman.append('sosis daging')
print("pizza faforit saya adalah:")
for pizza in pizza_saya:
    print(f"- {pizza}")
print("\npizza faforit teman saya adalah:")
for pizza in pizza_teman:
    print(f"- {pizza}")