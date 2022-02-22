# operasi aritmatika

# input user
print('='*10+'Input User')
a = int(input('variabel a: '))
b = int(input('variabel b: '))

# operasi tambah +
print('='*10+'Penjumlahan (+)')
print('a + b = ?')
hasil = a + b
print(a,'+', b, '=', hasil)

# operasi pengurangan -
print('='*10+'Penguarangan (-)')
print('a - b = ?')
hasil = a - b
print(a,'-', b, '=', hasil)

# operasi perkalian *
print('='*10+'Perkalian (*)')
print('a * b = ?')
hasil = a * b
print(a,'*', b, '=', hasil)

# operasi pembagian /
print('='*10+'Pembagian (/)')
print('a / b = ?')
hasil = a / b
print(a,'/', b, '=', hasil)

# operasi eksponen **
print('='*10+'Ekspoen (**)')
print('a ** b = ?')
hasil = a ** b
print(a,'**', b, '=', hasil)

# operasi modulus %, ket: sisa pembagian
print('='*10+'Modulus (%)')
print('a % b = ?')
hasil = a % b
print(a,'%', b, '=', hasil)

# operasi floor division //, ket: berapa kali bisa di bagi
print('='*10+'Floor division')
print('a // b = ?')
hasil = a // b
print(a,'//', b, '=', hasil)

## prioritas operasi, operational precedence
print('='*10+'Prioritas operasi')
x = 3
y = 2
z = 4
print(f'x = {x}, y = {y}, z = {z}')
# note urutan : (), exsponen, perkalian, pertambahan
print('-'*5+'contoh 1:')
print('x ** y * z + x / y - y % z // x = ?')
hasil = x ** y * z + x / y - y % z // x
print (x ,'**', y ,'*', z ,'+', x ,'/', y ,'%', z ,'//', x, '=', hasil)
print('-'*5+'contoh 2:')
print('( x + y ) * z = ?')
hasil = ( x + y ) * z
print('(',x, '+', y, ') *', z,'=', hasil)