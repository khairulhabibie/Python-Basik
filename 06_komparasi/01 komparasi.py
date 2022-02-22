# Operasi Komprasi : perbandingan data
'''
setiap hasil komparasi adalah boolean
simbol komparasi :
>, <, >=, <=, ==, !=, is, is not
'''
print ('='*10+'input variabel')
a = int(input("variabel a: "))
b = int(input("variabel b: "))

# lebih besar dari >
hasil = a > b
print(a, '>', b,'\t:',hasil)

# lebih kecil dari <
hasil = a < b
print(a, '<', 3,'\t:',hasil)

# lebih besar sama dengan dari >=
hasil = a > b
print(a, '=>', 3,'\t:',hasil)

# lebih kecil sama dengan dari <=
hasil = a <= b
print(a, '<=', 3,'\t:',hasil)

# sama dengan ==
hasil = a == b
print(a, '==', 3,'\t:',hasil)

# tidak sama dengan !=
hasil = a != b
print(a, '!=', 3,'\t:',hasil)

# Komparasi object indentity (is)
print ('='*10+'Komparasi Object Idetity (is)')
    # komparasi (is), contoh 1
x = 5  
y = 5
print('nilai x = ', x, ',id = ', hex(id(y)))
print('nilai y = ', y, ',id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)
    # komparasi (is), contoh 2
x = 5  
y = 6
print('nilai x = ', x, ',id = ', hex(id(y)))
print('nilai y = ', y, ',id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

# sebagai komparasi object identity (is not)
print ('='*10+'object idetity(is not)')
    # komparasi (is not), contoh 1
x = 5 
y = 5
print('nilai x = ', x, ',id = ', hex(id(y)))
print('nilai y = ', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)
    # komparasi (is not), contoh 2
x = 5
y = 6
print('nilai x = ', x, ',id = ', hex(id(y)))
print('nilai y = ', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)
