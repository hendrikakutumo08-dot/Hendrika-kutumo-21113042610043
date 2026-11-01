cities = {
    'jakarta': {
        'negara': 'indonesia',
        'populasi': '10 juta',
        'fakta': 'Kota ibu kota ekonomi negara.'
    },
    'tokyo': {
        'negara': 'jepang',
        'populasi': '37 juta',
        'fakta': 'Wilayah metropolitan terpadat di dunia.'
    },
    'paris': {
        'negara': 'prancis',
        'populasi': '2.1 juta',
        'fakta': 'Terkenal dengan sebutan kota mode dunia.'
    }
}
for kota, info_kota in cities.items():
    print(f"Kota: {kota.title()}")
    print(f"  Negara: {info_kota['negara'].title()}")
    print(f"  Populasi: {info_kota['populasi']}")
    print(f"  Fakta unik: {info_kota['fakta']}\n")