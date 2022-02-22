# string width and alignment

# data
data_nama = "khairul habibie"
data_umur = 23
data_tinggi = 170
data_nomor_sepatu = 44

# string
print('='*10+"Data string tanpa enter")
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(data_string)

print('='*10+"Data string dengan enter \\n")
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print(data_string)

# string multline dengan menggunakan enter atau newline
print('='*10+"Data string")
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print(data_string)

# string multiline (kutip triplets)
print('='*10+"Data string")
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}"""
print(data_string)

# mengatur lebar (>5 : rata kanan flash holder 5)
print('='*10+"Data string")
data_string = f"""nama   = {data_nama}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print(data_string)