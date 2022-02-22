# tipe data

# data integer : angka, tanpa koma
print('='*10+'Data Integer')
data_integer = 1
print("data : ", data_integer)
print("bertipe : ", type(data_integer))

# data float : angka, dengan koma
print('='*10+'Data Float')
data_float = 1.5
print("data : ", data_float)
print("bertipe : ", type(data_float))

# data string : karakter huruf
print('='*10+'Data String')
data_string = "khairul"
print("data : ", data_string)
print("bertipe : ", type(data_string))

# data boolean : terdiri dari "True atau False"
print('='*10+'Data Boolean')
data_bool = False                       # penulisan "F" harus besar, maupun "T" pada True
print("data : ", data_bool)
print("bertipe : ", type(data_bool))

# bilangan kompleks : terdiri dari bilangan real dan imajiner
print('='*10+'Data Kompleks')
data_complex = complex(5,6)
print("data : ", data_complex)
print("bertipe : ", type(data_complex))

# tipe data dari bahasa C
print('='*10+'Data Double (dari Bahasa C)')
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("bertipe : ", type(data_c_double))
'''
tida data double tidak tersedia di python
'''