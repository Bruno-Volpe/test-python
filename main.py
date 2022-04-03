from calculadora import soma

print(soma(10, 20))
print(soma(-10, 20))
print(soma(1.5, 2.5))
print(soma(15, 15))

try:
    print(soma('15', 15))
except AssertionError as e:
    print('Soima invalida', e)

try:
    print(soma('15', 15))
except TypeError as e:
    print('Soima invalida', e)