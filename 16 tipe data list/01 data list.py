# list (array)

# data list
print("="*10+"data 1 dan 2")
data1 = [1,4,9,16,25,36,49,64]
data2 = [200,500,700,900,1100,1200]
print("data1 =",data1)
print("data2 =",data2)

# indexing
print("="*10+"indexing")
subData1 = data1[3]
subData2 = data1[-3]
print("data1[3]:",subData1)
print("data2[-3]:",subData2)

# slicing
print("="*10+"slicing")
subData3 = data1[:4]
subData4 = data1[3:]
subData5 = data1[-3:]
print(subData3)
print(subData4)
print(subData5)

# aritmatika : penjumlahan
print("="*10+"penjumlahan")
data3 = data1 + data2
print(data3)

# copy konten list
print("="*10+"copy konten list")
a = data1[:]                # awal sampai akhir, menggunakan memory yang sama
print(a)
a[4] = 87                   # ubah data ke 4
print(data1)

# mengubah konten list
print("="*10+"mengubah konten list")
data1[3:5] = [11,12,13]     # ubah data ke 3 - 5 
print(data1)

# list dalam list
print("="*10+"list dalam list")
x = [data1,data2]           # matrik
print("list x:\n",x)

# akses list
print("="*10+"akses list dalam multi list")
y = x[0][3]                 # list pertama, index ke 3
z = x[1][5]                 # list keuda, index ke 5
print("list x:\n",x)
print("indeks x[0][3]:",y)
print("indeks x[1][5]:",z)

# method list
print("="*10+"method untuk list")
print(data1)
data1.append(30)
print(data1)

# hitung panjang list
print("="*10+"panjang list")
panjang_list = len(data1)
print(data1)
print(panjang_list)