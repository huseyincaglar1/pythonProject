for i in range(0, 11):
    print(i)
#o dan 10 a kadar yazdırır.

for i in range(0, 11, 2):
    print(i)
#0 dan 10 a kadar 2şer atlayarak yazdırır.

for i in range(10, -1, -2):
    print(i)
#10 dan 0 a doğru 2 azaltarak yazdırır

liste = ["as", True, 1.9, 5, ["asdsa", "sdf", "asssert"]]

for i in liste:
    print(i)
#listedeki elemanları sırayla yazdırır.

for i in liste[4]:
    print(i)
#listenin 4. indeksindeki elemanları sırayla yazdırır.

for i in range(0, 3):
    print(i)
else:
    print("for bitti")
#döngü bittiğinde else devreye girer.