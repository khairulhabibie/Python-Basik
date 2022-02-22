# for loop : perulangan

'''
for kondisi:
    aksi
'''
# Loop semua data di dalam list
print("="*10+"Loop Sebuah List")
angka_list = [0,2,4,8,10]
print("Angka list:",angka_list)

for i in angka_list: # code loop
    print(f"i sekarang --> {i}")
    
# Loop range
print("="*10+"Loop Range")
angka_range = range(1,5)
for i in angka_range:
    print(f"i sekarang --> {i}")

# Loop String
print("="*10+"Loop Karakter String")
data_str = "saya belajar python"
print("Kalimat String:",data_str)

for huruf in data_str:
        print(huruf)
