## menghitung speedUp Rise of Kingdom

print("Program hitung speedUp Rise of Kingdom".center(50,"="))
print(" ")
print("Masukkan jumlah speedUp anda !".center(50,"="))
print(" ")
# input jumlah speedUp
menit1 = float(input("\t\t 1 menit --> "))
menit5 = float(input("\t\t 5 menit --> "))
menit10 = float(input("\t\t10 menit --> "))
menit15 = float(input("\t\t15 menit --> "))
menit30 = float(input("\t\t30 menit --> "))
jam1 = float(input("\t\t 1 jam   --> "))
jam3 = float(input("\t\t 3 jam   --> "))
jam8 = float(input("\t\t 8 jam   --> "))
jam15 = float(input("\t\t15 jam   --> "))

# perhitungan
jumlah_menit = menit1 + (menit5*5) + (menit10*10) + (menit15*15) + (menit30*30) + (jam1 + (jam3*3) + (jam8*8) + (jam15*15))*60

jumlah_jam = jumlah_menit/60
jumlah_jam_menit = (float(jumlah_jam) - int(jumlah_jam))*60

jumlah_hari = (jumlah_menit)/(24*60)
jumlah_hari_jam = (float(jumlah_hari) - int(jumlah_hari))*24
jumlah_hari_jam_menit = ((float(jumlah_hari_jam) - int(jumlah_hari_jam))*60) + 1
    
print("\nJumlah speeUp anda :")
print(f"\t\t{int(jumlah_menit)} menit")
print(f"\tatau\t{int(jumlah_jam)} jam, {int(jumlah_jam_menit)} menit")
print(f"\tatau\t{int(jumlah_hari)} hari, {int(jumlah_hari_jam)} jam, {int(jumlah_hari_jam_menit)} menit")
print(" ")
print("Akhir dari program !".center(50,"="))