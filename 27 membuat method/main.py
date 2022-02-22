## class
class mahasiswa():
    nama = 'nama'

    def belajar(self, kondisi):
        print(self.nama,'sedang belajar',kondisi)
    
    def tidur(self):
        print(self.nama,'tidur di kelas')

## ini programnya 

habibie = mahasiswa()
khairul = mahasiswa()

habibie.nama = 'habibie'
khairul.nama = 'khairul'

# print(habibie.nama)
# print(khairul.nama)

habibie.belajar('dengan giat')   #ini disebut sebagai method
khairul.tidur()   #ini disebut sebagai method

