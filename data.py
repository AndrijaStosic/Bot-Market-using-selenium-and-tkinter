narudzbine = {}

def info(proizvod_entry, kolicina_spinbox):
    proizvod = proizvod_entry.get()
    kolicina = kolicina_spinbox.get()
    print(f"You ordered: {proizvod}, quantity: {kolicina}")
    narudzbine[proizvod] = kolicina
    print(narudzbine)
