nome1 = input("Qual è il tuo nome?\n")
nome2= input("Qual è il suo nome?\n")

nomi_combinati = nome1 + nome2
nomi_combinati_minuscoli = nomi_combinati.lower()

t_int = nomi_combinati_minuscoli.count("t")
r_int = nomi_combinati_minuscoli.count("r")
u_int = nomi_combinati_minuscoli.count("u")
e_int = nomi_combinati_minuscoli.count("e")

primo_numero = t_int + r_int + u_int + e_int

l_int = nomi_combinati_minuscoli.count("l")
o_int = nomi_combinati_minuscoli.count("o")
v_int = nomi_combinati_minuscoli.count("v")

secondo_numero = l_int + o_int + v_int + e_int

risultato = primo_numero*10 + secondo_numero

# il metodo Yoda di confronto utilizzo io
if (10 > risultato) or (90 < risultato):
    print(f"il vostro punteggio amoroso è {risultato}, lasciatevi!")
elif (40 >= risultato) or (50 <= risultato):
    print(f"il vostro punteggio amoroso è {risultato}, vi amerete per sempre")
else:
    print(f"il vostro punteggio amoroso è {risultato}")


