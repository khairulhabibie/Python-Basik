# Operator Assigment : operasi bitwise (LOGIKA)
'''
efisiensi penulisan logika
'''
# OR
print('='*10+"OR (|)")
c = True
print("nilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi: ",c)
c = False
print("nilai c =",c)
c |= True
print("nilai c |= False, nilai c menjadi: ",c)

# AND
print('\n'+'='*10+"AND (&)")
c = True
print("nilai c =",c)
c &= False
print("nilai c |= False, nilai c menjadi: ",c)
c = True
print("nilai c =",c)
c &= True
print("nilai c |= False, nilai c menjadi: ",c)

# XOR
print('\n'+'='*10+"XOR (^)")
c = True
print("nilai c =",c)
c ^= False
print("nilai c |= False, nilai c menjadi: ",c)
c = True
print("nilai c =",c)
c ^= True
print("nilai c |= False, nilai c menjadi: ",c)

# shifting
print('\n'+'='*10+" (>>)")
d = 0b0100
print("nilai d: ",format(d,'04b'))
    # ShiftRight
d >>= 2
print("nilai d: ",format(d,'04b'))
    # Shiftleft
d <<= 1
print("nilai d: ",format(d,'04b'))