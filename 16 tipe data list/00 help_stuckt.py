# melihat isi yang ada di dalam list

print(dir([]))
'''
'append', 'clear', 'copy', 'count', 'extend', 'index', 
'insert', 'pop', 'remove', 'reverse', 'sort'
'''

#help(list)
'''
append  : menambahkan data baru
    namalist.append(bisa string/angka)

clear   : menghapus list
    namalist.clear()

copy    : copy data list
    namalist2 = namalist.copy()

count   : hitung data yang ada di dalam list
    namalist.count(bisa string/angka)       #hitung jumlah string/angka dalam data string 

extend  : menambahkan data baru, ditulisan per karakter
    namalist.extend(bisa string/angka)

index   : indexing data di dalam list
    namalist.insert("string",3)             #menambahkan string pada index ke-3

insert  : menambahkan data pada index tertentu
    namalist[3]                             #index data dalam nama list pada index ke-3

remove  : menghapus data
    namalist.remove("string", angka)

pop     : hapus data pada bagian akhir list
    namalist.pop()
    
reverse : menukar data list, akhir ke awal
    namalist.resverse()

sort    : meurutkan list, dari data kecil ke besar
    namalist.sort()
'''