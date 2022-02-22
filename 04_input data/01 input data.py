# input_user

# data input akan dibaca sebagai "string"
print('='*10+'STRING')
data = input('Masukkan huruf: ')
print("data : ", data, ", type", type(data))

# data input akan dibaca sebagai "integer"
print('='*10+'INTEGER')
angka1 = int(input("Masukkan angka : "))
print("data : ", angka1, ", type", type(angka1))

# data input akan dibaca sebagai "float"
print('='*10+'FLOAT')
angka2 = float(input("Masukkan angka : "))
print("data : ", angka2, ", type", type(angka2))

# data input akan dibaca sebagai boolean
print('='*10+'BOOLEAN')
biner = bool(int(input("Masukkan huruf/angka : ")))
print("data : ", biner, ", type", type(biner))



