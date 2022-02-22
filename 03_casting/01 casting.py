# Casting : merubah tipe data

# casting integer
print('='*10+'Casting integer')
data_int = 9
print("data:", data_int, "\ttype:", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)                                  #akan nol jika nilai int = 0 
print("data:", data_float, "\ttype:", type(data_float))
print("data:", data_str, "\ttype:", type(data_str))
print("data:", data_bool, "\ttype:", type(data_bool))   #akan flase jika nilai int = 0

# casting float
print('='*10+'Casting Float')
data_float = 9.8
print("data:", data_float, "\ttype:", type(data_float))

data_int = int(data_float)                  #data akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)                #jika nilai float bukan nol akan bernilai True
print("data:", data_int, "\ttype:", type(data_int))
print("data:", data_str, "\ttype:", type(data_str))
print("data:", data_bool, "\ttype:", type(data_bool)) #akan false jika nilai float = 0

# casting boolean
print('='*10+'Casting Boolean')
data_bool = False
print("data:", data_bool, "\ttype:", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data:", data_int, "\ttype:", type(data_int))     #akan bernilai 0 karena bool "False", bila bool "True" akan benilai 1
print("data:", data_float, "\ttype:", type(data_float)) #akan bernilai 0 karena bool "False", bila bool "True" akan benilai 1
print("data:", data_str, "\ttype:", type(data_str))

#string
print('='*10+'Casting String')
data_str = "10"
print("data:", data_str, "\ttype:", type(data_str))

data_int = int(data_str)                        #string harus angka
data_float = float(data_str)                    #string harus angka
data_bool = bool(data_str)                      #false jika string kosong
print("data = ", data_int, "\ttype = ", type(data_int))
print("data = ", data_float, "\ttype = ", type(data_float))
print("data = ", data_bool, "\ttype = ", type(data_bool))