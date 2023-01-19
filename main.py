# Este programa identifica pangramas, que son frases que contienen todas
# las letras del alfabeto (a-z), ignorando mayusculas y el orden
# El tiempo de ejecucion es O(n), siendo n el numero de caracteres de s (el input)

s = 'abcdefghijklmnopqrstuvvwxyz,'
# s = 'The quick, brown fox jumps over the lazy dog!'
# s = '1bcdefghijklmnopqrstuvwxyz'

alphabet = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for c in s:
    value = ord(c.lower()) - 97
    if value in range(0, 26):
        alphabet[value] = 1

result = 1

for elem in alphabet:
    result *= elem

print(result)