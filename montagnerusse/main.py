print("Benvenuto alle montagne russe!\n ")

altezza_in_cm = input("Qual è la tua altezza in cm?\n")
altezza_in_cm_int = int(altezza_in_cm)

costo_del_biglietto_in_USD = 0

if altezza_in_cm_int > 120:
    print("puoi salire sulle montagne russe\n")
    
    età = input("Quanti anni hai?\n")
    età_int = int(età)
    if età_int > 18:
        print("il biglietto costa $12\n")
        costo_del_biglietto_in_USD += 12
    elif età_int > 12:
        print("il biglietto costa $7\n")
        costo_del_biglietto_in_USD +=7
    else:
        print("il biglietto è $5\n")
        costo_del_biglietto_in_USD += 5

    richiesta_foto = input("Vuoi la foto? s\\n\n")
    if richiesta_foto == "s":
            costo_del_biglietto_in_USD += 3

    print(f"il costo totale del biglietto è: ${costo_del_biglietto_in_USD}\n")
    

else:
    print("non puoi salire")