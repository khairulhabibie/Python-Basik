## function

def suaraAyam():
    print("kukuruyuuk!!!!")

def hargaAyam():
    print("harga ayam per 1 kilogram adalah Rp.20.000")

def hargaTotalAyam(kg):
    suaraAyam()
    harga = 20000
    hargaTotal = kg*harga
    print("harga",kg,"kilogram ayam adalah Rp.",hargaTotal)

# memanggil fungsi
hargaAyam()
hargaTotalAyam(2)
hargaTotalAyam(0.5)
hargaTotalAyam(5)
hargaTotalAyam(7)