# shifting

# variabel a dan b
print('='*10+'nilai a dan b')
a = 9
b = 5
print("nilai :", a, ", binary :", format (a,"08b"))
print("nilai :", b, ", binary :", format (b,"08b"))

# shifright (>>) : menggeser binary ke kanan
c = a >> 2
print('='*10+'shiftright: (a>>2)')
print("nilai :", c, ", binary :", format (c,"08b"))

# shifleft (<<) : menggeser binary ke kiri
c = a << 2
print('='*10+'shifleft: (a<<2)')
print("nilai :", c, ", binary :", format (c,"08b"))