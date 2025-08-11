narudzbine = {}

def info(proizvod_entry, kolicina_spinbox):
    proizvod = proizvod_entry.get().strip()
    kolicina = kolicina_spinbox.get().strip()
    
    if proizvod and kolicina:
        print(f"Narucili ste: {proizvod}, kolicina: {kolicina}")
        narudzbine[proizvod] = kolicina
        print(f"Trenutne narudzbine: {narudzbine}")
    else:
        print("Greska: naziv proizvoda ili kolicina je prazna!")

def uzmi_narudzbine():
    return narudzbine.copy()

def ocisti_narudzbine():
    narudzbine.clear()
    print("Sve narudzbine obrisane!")

def ukloni_narudzbinu(proizvod):
    if proizvod in narudzbine:
        del narudzbine[proizvod]
        print(f"Uklonjen {proizvod} iz narudzbina")
        return True
    return False
