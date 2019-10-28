w=int(input("Podaj wysokość piramidy: "))
g=1
while w>0:
    print((w-1) * " " + (g * "#"))
    w-=1
    g+=2