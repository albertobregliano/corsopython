import sys

print("Benvuto nel calcolatore di indice di massa corporea BMI\n")

peso_in_kg = input("quanto pesi in Kg?\n")
peso_in_kg_int = int(peso_in_kg)
if peso_in_kg_int > 1_000:
    print("sei decisamente obeso il calcolo del BMI non ha senso")
    sys.exit

altezza = input("quanto sei alto in cm?\n")
altezza_in_cm_float = float(int(altezza) /100)
if altezza_in_cm_float > 3:
    print("sei più alto di un vatusso! Per te il BMI non ha senso")
    sys.exit()

bmi_float = peso_in_kg_int / (altezza_in_cm_float**2)
bmi_float_rounded = round(bmi_float, 2)

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

print(f"sei alto {altezza_in_cm_float}cm e pesi {peso_in_kg}kg e il tuo indice di massa corporea è: {bmi_float_rounded} quindi sei {risultato}")