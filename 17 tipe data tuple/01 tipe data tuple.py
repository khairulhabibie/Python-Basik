# tipe data tuple

print("="*10+"data tuple")
# tuple
genap = (2,4,6,6,6,6,8,10)
print(type(genap))
print(dir(genap))   # Melihat apa saja yang ada di 'TUPLE'

print(genap)
print("count:",genap.count(6)) # hitung jumlah angka '6'
print("index:",genap.index(8)) # lihat posisi angka '8'

# perbedaan data tuple dan list
"""
list [] --> bisa diubah datanya
tuple ()--> tidak bisa di ubah datanya, 
            ukuran data lebih ringan dari list
            waktu running program lebih cepat dari list
"""


