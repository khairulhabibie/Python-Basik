## operasi logika atau boolean
'''
logika : 
not, or, and, xor
'''

# NOT (not)
print('='*10+'NOT')
a = True
b = not a
print('data a:', a)
print('data b = not a:', b)

# OR (or)
print('='*10+'OR')
a = False 
b = False
c = a or b
print (a, 'OR', b, '=', c)
a = True 
b = False
c = a or b
print (a, 'OR', b, '=', c)
a = False 
b = True
c = a or b
print (a, 'OR', b, '=', c)
a = True 
b = True
c = a or b
print (a, 'OR', b, '=', c)

# AND (and)
print('='*10+'AND')
a = False 
b = False
c = a and b
print (a, 'OR', b, '=', c)
a = True 
b = False
c = a and b
print (a, 'OR', b, '=', c)
a = False 
b = True
c = a and b
print (a, 'OR', b, '=', c)
a = True 
b = True
c = a and b
print (a, 'OR', b, '=', c)

# XOR (^)
print('XOR'.center(30,'-'))
a = False 
b = False
c = a ^ b
print (a, 'OR', b, '=', c)
a = True 
b = False
c = a ^ b
print (a, 'OR', b, '=', c)
a = False 
b = True
c = a ^ b
print (a, 'OR', b, '=', c)
a = True 
b = True
c = a ^ b
print (a, 'OR', b, '=', c)