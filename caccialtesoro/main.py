line1 = ["😛","😛","😛"]
line2 = ["😛","😛","😛"]
line3 = ["😛","😛","😛"]

map = [line1, line2, line3]

coordinate = input()

abc = ["a","b","c"]

lettera = coordinate[0].lower()
x = abc.index(lettera)
y = int(coordinate[1]) -1

map[y][x] = "😡"

print(f"{line1}\n{line2}\n{line3}")