## teknik looping

# loop biasa
print("="*10+"loop biasa")
for i in range (0,4,1):
    print(i)

# reversed : loop dari data akhir ke awal
print("="*10+"reversed")
for i in reversed(range(0,4,1)):
    print(i)

# enumarete : 
print("="*10+"enumerete") 
nama_jurusan = ["fisika",
                "kimia",
                "biologi",
                "matematika",
                "elektro"]               
for index, jurusan in enumerate (nama_jurusan):
    print(index,':',jurusan)

# zip :
print("="*10+"ZIP") 
nama_jurusan = ["fisika",
                "kimia",
                "biologi",
                "matematika",
                "elektro"]               
nama_pelajaran = ["kuantum",
            "partikel",
            "sel makhluk hidup",
            "kalkulus",
            "rangkaian listrik"]
for jurusan, belajar in zip (nama_jurusan,nama_pelajaran):
        print(belajar,"dipelajari dalam jurusan:",jurusan)

# data set :  
print("="*10+"set")
nama_jurusan = {"fisika",
                "kimia",
                "biologi",
                "matematika",
                "elektro"}
for jurusan in sorted(nama_jurusan):        # meng-urutkan data
    print(jurusan)
    
# data dictionary
print("="*10+"dictionary")
sains = {"fisika": "kuantum",
            "kimia":"partikel",
            "biologi":"sel makhluk hidup",
            "matematika":"kalkulus",
            "elektro":"rangkain listrik"}
for i,v in sains.items():
    print(i,"memiliki mata kuliah",v)