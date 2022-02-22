## tipe data dictionary

"""
print(member1.keys())
print(member1.values())
print(member1.items())
"""

member1 = {"ID":101,
            "nama":"habibie",
            "status member":"gold"}

member2 = {"ID":102,
            "nama":"khairul",
            "status member":"silver"}
            
memberlist = {101:member1,102:member2}

print(memberlist[101])
print(memberlist[102])
