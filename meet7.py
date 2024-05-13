# Tabel Kebenaran (logika bolean)
# not and or xor

#NOT
print("*****Logika NOT*****")
x = False
y = True
print('value x =', x)
print('***********NOT')
print('value y =', y)

#OR
print("*****Logika OR*****")
x = False
y = False
z = x or y
print(x, 'OR', y, '=', z)

x = False
y = True
z = x or y
print(x, 'OR', y, '=', z)

x = True
y = False
z = x or y
print(x, 'OR', y, '=', z)
x = True
y = True
z = x or y
print(x, 'OR', y, '=', z)

#AND ()
print("*****Logika AND*****")
x = False
y = False
z = x or y
print(x, 'and', y, '=', z)

x = False
y = True
z = x or y
print(x, 'and', y, '=', z)

x = True
y = False
z = x or y
print(x, 'and', y, '=', z)
x = True
y = True
z = x or y
print(x, 'and', y, '=', z)

# XOR
print("*****Logika XOR*****")
x = False
y = False
z = x or y
print(x, 'XOR', y, '=', z)

x = False
y = True
z = x or y
print(x, 'XOR', y, '=', z)

x = True
y = False
z = x or y
print(x, 'XOR', y, '=', z)
x = True
y = True
z = x or y
print(x, 'XOR', y, '=', z)




