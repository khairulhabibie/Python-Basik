# Operator Bitwise (LOGIKA) ~> operasi masing masing bit

# variabel a dan b
print('='*10+'nilai a dan b')
a = 9
b = 5
print("nilai :", a, ", binary :", format (a,"08b"))
print("nilai :", b, ", binary :", format (b,"08b"))

# bitwise OR (|)
c = a | b
print('='*10+'OR: (a|b)')
print("nilai:", c, ", binary :", format (c,"08b"))

# bitwise AND (&)
c = a & b
print('='*10+'AND: (a&b)')
print("nilai:", c, ", binary :", format (c,"08b"))

# bitwise XOR (^)
c = a ^ b
print('='*10+'XOR: (a^)b')
print("nilai:", c, ", binary :", format (c,"08b"))

# bitwise NOT (~)
c = ~a
print('='*10+'NOT: (~a)')
print("nilai:", c, ", binary :", format (c,"08b"))