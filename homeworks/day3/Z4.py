#Zamiana liczb bin na dec

from whatnext import start_other_module

print("\n*** To jest program do zamieniania liczb bin na dec ***\n")

num=str(input("Podaj dowolną liczbę binarną:  "))
right_values = ["0", "1"]

a = 0

for x, d in enumerate(num[::-1]): # binnary jest enumerowane od tyłu
      if d == "1":
          a += (2**x)

      elif d == "0":
          continue

      else:
            print('Podana liczba nie jest liczbą binarną')

if a > 0:
      print(a)
else:
      pass

start_other_module("multitool")

