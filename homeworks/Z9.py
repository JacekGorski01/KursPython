print('Dowiedz się ile "ludzkich" lat ma Twój pies')
dog_age=float(input("Wpisz ile lat ma Twój pies: "))

if dog_age <= 2:
        man_age = dog_age * 10.5


else:
        man_age = 21 + (dog_age - 2) * 4

print(f'Twój pies ma {man_age} "ludzkich" lat.')