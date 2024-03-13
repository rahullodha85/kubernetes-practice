from camelcase import CamelCase
c = CamelCase()
s = 'this is a sentence that needs CamelCasing!'

print('Original:', s)
print('---------------------')
print('Camelcase:', c.hump(s))
