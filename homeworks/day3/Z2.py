from whatnext import start_other_module

print("\n*** To jest program do przedstawienia pierwszej i ostatniej cyfry podanej liczby ***\n")

num=float(input("Podaj dowolną liczbę:  "))
num=round(num)
snum = str(num)

print(f"Pierwsza cyfra podanej liczby to: {snum[0]}, a ostatnia to {snum[-1]}\n")

start_other_module("multitool")