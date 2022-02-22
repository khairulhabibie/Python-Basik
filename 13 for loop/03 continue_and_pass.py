# continue dan pass

# loop
print("="*10+"Loop")
for i in range (1,10):
    print(i)
else:
    print("akhir dari loop")

# loop dengan break
print("="*10+"Loop,break")
for i in range (1,10):
    print(i)
    if i is 6:
        print("nilai saat ini")
        break
else:
    print("akhir dari loop")

# loop dengan continue    
print("="*10+"Loop,continue")
for i in range (1,10):
    print(i)
    if i is 6:
        print("nilai saat ini")
        continue
else:
    print("akhir dari loop")

# diluar loop
print("="*10+"diluar Loop")
print("ini diluar loop")