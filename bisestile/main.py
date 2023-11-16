anno = input("Quale anno vuoi sapere se è bisestile o meno?\n")
anno_int = int(anno)

divisibile_per_4_bool = anno_int % 4 == 0
divisibile_per_100_bool = anno_int % 100 == 0
divisibile_per_400_bool = anno_int % 400 == 0

result = (divisibile_per_4_bool & ~divisibile_per_100_bool) | divisibile_per_400_bool

if result:
    print(f"l'anno {anno} è bisestile\n")
else:
    print(f"l'anno {anno} NON è bisestile\n")
