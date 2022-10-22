liste = ["Elma", "Armut", "Ayva"]

a = liste.copy() # listeyi kopyalar
b = list(liste) # listeyi kopyalar
print(a);print(b)

liste.sort() # bu metod liste elemanlarını küçükten büyüğe doğru sıralar.
print(liste) # burada alfabetik olarak sıralar.

liste.reverse() # elemanları büyükten küçüğe doğru sıralar.
print(liste)

print(min(liste)) # min elemanı gösterir.

print(max(liste)) # max elemanı gösterir.

def fonksiyon(n):
  return abs(n - 50) # abs() metodu sayıların mutlak değerlerini alır.

sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon) 
print(sayi_listesi)