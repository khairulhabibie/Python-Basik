# manipulasi list 

# list1
barang = ["kunci","ember","jaket","ban","mobil"]
print(barang)
# manipulasi list
    # menambah data ke dalam list
barang.append("sepeda")
print(barang)

barang.extend("dompet")
print(barang)

barang.insert(3,"sepeda") # insert di nomor 3
print(barang)

    # menghitung anggota
jumlahSepeda = barang.count("sepeda")
print("jumlah sepeda adalah:",jumlahSepeda)

    # me-remove data
barang.remove("sepeda")
print(barang)

print("="*50)

# list2
barang2 = barang.copy() # agar tidak menggunakan referensi yang sama
barang2.append("gelas") # data pada "barang tidak berubah karena menggunakan referensi yang sama"
print(barang)
print(barang2)