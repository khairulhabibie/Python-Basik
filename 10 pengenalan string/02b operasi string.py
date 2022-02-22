# operasi dalam bentuk method

# merubah case dari string
'''
upper case : semua huruf kapital
lower case : semua huruf kecil
proper case : setiap awal kata kapital 
'''
print('='*10+'merubah case string')
salam = "aLAy"
print("normal = " + salam)
    # ubah ke UPPER case
salam = salam.upper()
print("upper = " + salam)
    # ubah ke lower case
salam = salam.lower()
print("lower = " + salam)
    # ubah ke Proper case : setiap awal kata adalah kapital
salam = salam.title()
print("proper = " + salam)

# pengecekan (isX) method:: hasilnya boolean
print('='*10+'pengecekan method')
salam = "sist"
apakah_lower = salam.islower()
    # apakah lower case ?
print(salam + " is lower = " + str(apakah_lower))
    # apakah upper case ?
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))
    # apakah proper ?
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

'''
methode lainnya:
isalpha() <-- mengecek semuanya huruf
isalmum() <-- huruf dan angka
isdecimal() <-- angka saja
isspace() <-- spasi, tab, newline \n
istitle() <-- semua kata dimulai dengan huruf besar
'''

# cek komponen startswith() endswith() <-- keren
print("="*10+"cek komponen")
cek_start = "Salam satu Unpad".startswith("Salam")
print("start = " + str(cek_start))
cek_end = "Salam satu Unpad".endswith("Unpad")
print("end = " + str(cek_end))

# penggabungan komponen: join() split()
print("="*10+"penggabungan komponen")
data = ['aku', 'sayang', 'kamu']        # data list
print(data)
gabung = ','.join(data)
print(gabung)
gabung = ' '.join(data)
print(gabung)
gabung = ' ehm '.join(data)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))

# alokasi karakter : rjust(), ljust(), center()
print("="*10+"alokasi karakter")
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(10)
print("'"+tengah+"'")
tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebalikan --> strip()
tengah = tengah.strip(":")              # menghilangkan tanda :
print("'"+tengah+"'")