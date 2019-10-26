#wyrazy = ["jeden", "dwa", "trzy"]
#wyrazy[0] = "raz"
#print(wyrazy)

# liczby_parzyste = range(0,20,2)
# print(liczby_parzyste)
# if 9 in liczby_parzyste:
#     print("Prawda")
#
# else:
#     print("Nie prawda")
#
# lista_liczb_parzystych = list(range(0,20,2))
# print(lista_liczb_parzystych)

zakupy = ["kiełbasa", "piwko", "chipsy", "węgiel", "kubeczki"]
print(zakupy)
zakupy.append("talerzyki")
print(zakupy)
zakupy.insert(0,"serwertki")
print(zakupy)
zakupy[0] = "serwatka"
print(zakupy)
zakupy.remove("piwko")
print(zakupy)

for przedmiot in zakupy:
    if przedmiot == 'węgiel':
        znak = '[x] '
    else:
        znak ='[] '
    print(znak + przedmiot)


# x=0
# print("Start")
# while x<10:
#     x+=1
#     zdanie = f"Jestem w pętli  {x}"
#     print(zdanie)