# operasi string

# menyambungkan beberapa string (concatenate)
print("="*10+"menyambungkans string")
nama_pertama = "khairul"
nama_tengah = "D"
nama_akhir = "Habibie"
print("nama_pertama:",nama_pertama)
print("nama_tengah:",nama_tengah)
print("nama_akhir:",nama_akhir)
nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print("print_lengkap:",nama_lengkap)

# menghitung panjang string
print("="*10+"menghitung panjang string")
panjang = len(nama_lengkap)
print("panjang list adalah:",panjang)

# cek suatu char atau string di dalam string
print("="*10+"cek char/string di dalam string")
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + ": " + str(status))

d = "D"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + ": " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " ada di " + nama_lengkap + ": " + str(status))
# pengulangan
print("="*10+"pengulangan")
print("wk"*10)
print(15*"wk")
# indexing
print("="*10+"indexing")
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-5 : " + nama_lengkap[5])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-(0:4) : " + nama_lengkap[0:5])
print("index ke-(0,2,4,6,8,10) : " + nama_lengkap[0:10:2]) #ambil char beda 2 char

print("="*10+"cek karakter maksimum dan minimum")
    # item paling besar
print("paling besar : " + max(nama_lengkap))
    # item paling kecil
print("paling kecil : " + min(nama_lengkap))

data = 117
print("ASCII code untuk data adalah : " + chr(data))
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))

# operasi dalam bentuk method
print("="*10+"operasi dalam bentuk method")
data = "orang minang babaso baso makan bakso di solo"
jumlah = data.count("o")
print("jumlah o",data,"adalah:",jumlah)