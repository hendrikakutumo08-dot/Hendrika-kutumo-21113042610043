def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

mobil_baru = make_car(
    'toyota', 'avanza',
    warna='hitam',
    fitur_opsional='sunroof'
)
print(mobil_baru)