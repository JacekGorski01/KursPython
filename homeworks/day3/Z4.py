num=str(input("Podaj dowolną liczbę binarną:  "))
#num=int(num)
#print(int(num, 2))

binnary = str(num)
rev=(binnary[::-1])
a = 0
print(rev)

for x, d in enumerate(rev):
      if d == "1":
        a += (2**x)

      elif d != "0" and d != "1":
            a="!!!"
            print(f"Podana liczba nie jest liczbą binarną {a}")
            break



print(a)

