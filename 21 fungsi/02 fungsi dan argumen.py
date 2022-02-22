## function and argument

# fungsi dengan argument sederhana
print("="*10+"fungsi dengan argument sederhana")
def siswa(nama):
	print("mahasiswa ini bernama:",nama)
	
siswa("habibie")

# fungsi dengan keyword argument
print("="*10+"fungsi dengan keyword argument")
def dosen(nama,matkul):
    print("dosen ini bernama:",nama)
    print("mengajar matakuliah:",matkul)

dosen(nama="ayi",matkul="fisika material")              # keyword argument

# fungsi dengan default argument
print("="*10+"fungsi dengan default argument")
def penjagaKampus(nama,shift="siang",sifat="ramah"):    # default argument
    print("penjaga kampus ini bernama:",nama)
    print("shiftnya:",shift)
    print("sifat:",sifat)

penjagaKampus("endang")

penjagaKampus("toyyib",shift="malam")

penjagaKampus("otong",sifat="galak")