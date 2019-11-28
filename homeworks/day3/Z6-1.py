lista = ["1111", "1111111111111", "111", "222", "222", "33333333333333333","hurrrraaaaaa!"]
#print(type(lista[0]))
#print(lista)
no_elements = len(lista) # ile lista ma elementów (liczba column)
#print(no_elements)
longest = max(lista, key = len) #żeby zawsze była ta sama szerokość musi byc znany najdłuższy element
maxlong = (len(longest))
#maksymalna długość stringa z listy
if maxlong > 10:
    maxlong = 10
else:
    pass

width=(len(longest)) * no_elements
#print(width)

#Drukowanie pierwszego wiersza z rozróżnieniem czy to jest ostatni element, żeby dostawić "+"
def top_bottom_line(lista,no_elements,maxlong):
    for x, d in enumerate(lista):
        if x == no_elements-1:
            print("+" + maxlong * "-" + "+")
        else:
            print("+" + maxlong  * "-", end='')


top_bottom_line(lista,no_elements,maxlong)
#Drukowanie elementów listy
for x, d in enumerate(lista):
    if len(d) < maxlong and x != no_elements -1:
            x = maxlong - len(d)
            print("|" + d + x * " ", end='')

    elif len(d)<maxlong  and x == no_elements-1:
            x = maxlong - len(d)
            print("|"+ d + x * " " + "|")

    elif len(d) == maxlong and x == no_elements - 1:
            print("|" + d + "|")

    elif len(d) > maxlong and x != no_elements - 1:
            d=d[0:7]
            print("|" + d + "...", end='')

    elif len(d) > maxlong and x == no_elements - 1:
            d=d[0:7]
            print("|" + d + "...|" )

    else:
            print("|" + d, end='')
#Drukowanie ostatniego wiersza z rozróżnieniem jak pierwszy
top_bottom_line(lista,no_elements,maxlong)