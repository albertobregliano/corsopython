import random

n = input("Inserisci lunghezza password:\n")
n_int = int(n)

if n_int > 21:
    n_int = 21

if n_int < 12:
    n_int=12

alfabeto = "abcdefghiljkmnopqrstuvwxyz"
numeri = "0123456789"
segni = """!"£$%&/()=?-_^+#@"""

password = ""

for i in range(1, 3):
    password += random.choice([*alfabeto]).upper()

for i in range(1, 3):
    password += random.choice([*numeri])

for i in range(1, 3):
    password += random.choice([*segni])

for i in range(1, n_int-6):
    password += random.choice([*alfabeto])


list_pass = list(password)
random.shuffle(list_pass)
result = ''.join(list_pass)
print(result)

