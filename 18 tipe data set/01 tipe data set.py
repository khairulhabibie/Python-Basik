# tipe data set
"""
data set :
karakteristik --> tipe data himpunan (tidak mementingkan urutan)
"""

print("="*10+"penulisan : cara 1")
# cara 1
superhero = {"regressor",
            "returner"
            }
superhero.add("khairul")
superhero.add("habibie")

print(superhero)

print("="*10+"penulisan : cara 2")
# cara 2
hero = set()
hero.add("habibie")
hero.add("khairul")
hero.add("returner")
hero.add("regressor")

print(hero) # tidak support indexing

print("="*10+"penulisan : cara 3")
ganjil = {1,3,5,7,9,11}
genap = {2,4,6,8,10}
prima = {1,2,3,5,7,11}

print("ganjil:",ganjil)
print("genap:",genap)
print("prima:",prima,"\n")

print("gabungan ganjil dan genap:",ganjil.union(genap)) #gabungan data(math)
print("irisan ganjil dan prima:",ganjil.intersection(prima)) #irisan data (math)