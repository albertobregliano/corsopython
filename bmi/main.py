peso_in_kg = input("quanto pesi in Kg?\n")
altezza = input("quanto sei alto in cm?\n")

altezza_in_cm = float(int(altezza) /100)

bmi_float = round(int(peso_in_kg) / (altezza_in_cm**2), 2)

risultato = ""

if bmi_float > 35:
    risultato = "seriamente obeso"
elif bmi_float > 30:
    risultato = "obeso"
elif bmi_float > 25:
    risultato = "sovrappeso"
elif bmi_float > 18.5:
    risultato = "normopeso"
else:
    risultato = "sottopeso"


#f-String
print(f"sei alto {altezza_in_cm}cm e pesi {peso_in_kg}kg e il tuo indice di massa corporea è: {bmi_float} quindi sei {risultato}")