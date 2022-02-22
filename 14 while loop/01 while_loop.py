# while loop : perulangan
'''
while kondisi:  # kondisi dalam boolean
    aksi 1
    aksi 2
'''
# tipe 1
print("="*10+"while loop - type 1")
angka = 0
print(f"angka sekarang: {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang: {angka}")
print("akhir dari program")
    
# tipe 2
print("="*10+"while loop - type 3")
angka = 0
while angka < 5:
    print(f"angka saat ini: {angka}")
    angka += 1
else:
    print(f"nilai angka dari loop: {angka}")
    
# tipe 3
print("="*10+"while loop - type 2")
start = True
print(f"start= {start}")
while start:
    print(f"ini di dalam loop, start = {start}")
    if angka is 10:
        start = False
        print(f"angka ditemukan, start = {start}")
    angka += 1

