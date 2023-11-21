import random

nomi_sring = "Alberto, Gino, Pino, Lino, Dino"
nomi = nomi_sring.split(", ")

num = random.randint(0,len(nomi)-1)

print(f"Oggi paga {nomi[num]}!\n")