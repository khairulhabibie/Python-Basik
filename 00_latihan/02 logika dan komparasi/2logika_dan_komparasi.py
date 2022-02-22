## latihan logika dan komparasi

# membuat gabingan area rentang dari angka

## +++++3-------10+++++
inputUser = float(input("Masukkan akang yang\nkurang dari 3 atau lebih besar dari 10: "))

# -------3 
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3: ", isKurangDari)

# -------10
# memerika angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 3: ", isLebihDari)

# kurang dari 3 atau lebih dari 10
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

## -----3+++++++10-----
# kasus irisan

inputUser = float(input("\nMasukkan akang yang lebih dari 3 atau kurang dari 10: "))
# -----3+++++++
# lebih dari 3
isLebihDari = inputUser > 3
print ("lebih dari 3: ", isLebihDari)

# kurang dari 3
isKurangDari = inputUser < 10
print ("kurang dari 3: ", isKurangDari)

# libih dari 3 atau kurang dari 10
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect)

