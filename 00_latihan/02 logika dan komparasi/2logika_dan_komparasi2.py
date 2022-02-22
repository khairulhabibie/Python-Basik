## latihan

## soal nomor 1
inputUser = float(input("Masukkan angka (0 < angka < 5) atau (8 < angka < 11): "))
# bagian pertama
isLebihDari = inputUser > 0
isKurangDari = inputUser < 5
isCorrect = isLebihDari and isKurangDari
print("angka > 0: ", isLebihDari)
print("angka < 5: ", isKurangDari)
print("0 < angka < 5 : ", isCorrect)

# bagian kedua
isLebihDari2 = inputUser > 8
isKurangDari2 = inputUser < 11
isCorrect2 = isLebihDari2 and isKurangDari2
print("angka > 8: ", isLebihDari2)
print("angka < 10: ", isKurangDari2)
print("8 < angka < 10 : ", isCorrect2)

# bagian ketiga
isCorrect3 = (isCorrect) or (isCorrect2) 
print("Angka yang anda masukkan: ", isCorrect3)


## soal nomor 2
inputUser = float(input("\nMasukkan angka angka < 0 atau (5 < angka < 8) atau angka > 11: "))
# bagian pertama
isKurangDari = inputUser < 0
isLebihDari = inputUser > 5
isKurangDari2 = inputUser < 8
isCorrect = isLebihDari and isKurangDari2
isLebihDari2 = inputUser > 11
isCorrect2 = ((isKurangDari or isCorrect) or (isLebihDari2)) 
print("angka < 0: ", isKurangDari)
print("5 < angka < 8 : ", isCorrect)
print("angka > 11: ", isLebihDari2)
print("angka < 0 atau (5 < angka < 8) atau angka > 11 : ", isCorrect2)