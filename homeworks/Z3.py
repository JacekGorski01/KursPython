w=int(input("Podaj szerokość prostokąta: "))
h=int(input("Podaj wysokość prostokąta: "))

print("+" + (w-2) * "-" + "+")
while h > 2:
    print("|" + (w-2) * " " + "|")
    h-=1
print("+" + (w-2) * "-" + "+")