# scope global dan lokal

# variabel global
nama = "habibie"

print("="*10+"scope local")

def ubahNama(namaBaru):
    nama = namaBaru #variable local
    print("saya ubah nama menjadi:",nama)

ubahNama("khairul")
print("nama saya adalah:",nama)

print("="*10+"scope global")

def ubahNama(namaBaru):
    global nama     #ambil varible global
    nama = namaBaru #nama menjadi varibel global, terjadi perubahan data pada varibel global
    print("saya ubah nama menjadi:",nama)

ubahNama("khairul")
print("nama saya adalah:",nama) #nama sudah di tukar menjadi "khairul" saat memanggil fungi "ubahNama"

