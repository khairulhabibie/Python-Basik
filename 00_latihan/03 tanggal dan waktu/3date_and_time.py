## latihan date and time

import datetime as dt
print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal\t: "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun\t: "))

tanggal_lahir =  dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}\n")
print (f"Hari nya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Hari ini tanggal : {hari_ini}")
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan} bulan")