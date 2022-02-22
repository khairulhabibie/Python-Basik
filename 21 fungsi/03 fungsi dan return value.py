# fungsi : dengan return value

print("="*10+"return value")
# fungsi dengan return value 
def kuadrat(argument):
    total = argument**2
    print("nilai kuardrat dari",argument,"adalah",total)
    return total                                            # menulis return untuk mendapatan retunr value

a = kuadrat(3)
print(a)

print("="*10+"return value dan multiple argument")
# fungsi dengan teturn value dan multiple argument
def tambah(argument1,argument2):                            # cara penambahan argumen pada fungsi
    total = argument1 + argument2
    print(argument1, "+", argument2,"=",total)
    return total

def kali(argument1,argument2):
    total = argument1 * argument2
    print(argument1, "x", argument2,"=",total)
    return total

b = kali(3,tambah(3,4))                                      # jumlah argumen harus sama dengan argumen pada fungsi, kecuali pada fungsi ada argumen default sehingga argument tersebut bisa tidak ditulisakn dalam fungsi
print(b)