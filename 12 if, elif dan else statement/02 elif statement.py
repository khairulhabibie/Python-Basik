## elif adalah: else if

'''
if kondisi:
    aksi
elif kondisi:
    aksi
elif kondisi:
    aksi
else:
    aksi
'''
nama = input("input (habibie/khairul):? ")
if nama == "khairul":
    print(f"hai {nama}, apa kabar ?")
elif nama == "habibie":
    print(f"hai {nama}, apa kamu sudah makan ?")
else:
    print("hmm..., kamu bukan khairul atau habibie ya")