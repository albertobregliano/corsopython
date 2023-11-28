import random

# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
map =[rock, paper, scissors]


print(f"Scegli [p]ietra [c]arta o [f]orbice")

scelta_map = ["p","c","f"]
scelta_utente_str = input().lower()
scelta_utente_int = scelta_map.index(scelta_utente_str)

scelta_pc_int = random.randint(0, 2)
print(f"Hai scelto:\n{map[scelta_utente_int]} e il pc ha scelto:\n{map[scelta_pc_int]}")

if scelta_utente_int == scelta_pc_int:
    print("Parità\n")
elif scelta_pc_int == scelta_utente_int +1:
    print("Hai perso\n")
elif scelta_pc_int == scelta_pc_int + 2:
    print("Hai vinto\n")
else: print("Hai perso!")

