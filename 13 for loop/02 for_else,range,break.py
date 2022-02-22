# for else, range,break

number = 25 ##ubah ini untuk kondisi
for i in range (0,41):
    print(i)
    if i is number:
     print("angka ditemukan", i)
     break
else:
    print("angka tidak ditemukan")
    
print("space di luar for")