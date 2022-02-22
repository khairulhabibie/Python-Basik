## input dan output file

## membuat file text

'''
w = write mode / mode menulis dan menghapus file lama
r = read mode / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write dan read mode
'''
## membuat text
# file = open("data.txt", 'w')
# file.write("baris ini ada di python")
# file.write('\nini barisa kedua')
# file.write('\nini barisa ketiga')
# file.write('\nini barisa keempat')
# file.close()

## membaca file text
# file2 = open('data.txt','r')
# # print(file2.read())
# # print(file2.read(10))  # baca hanya 10 karakter
# print(file2.readline())
# file2.close()

## appending file
file3 = open('g:''data.txt', 'a')
file3.write('\nbaris ini dibuat dengan menggunakan mode append')
file3.close()
