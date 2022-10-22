a = [1, 6]
a.append(5) # yeni elemanı listenin en sonuna ekler.
print(a)

a.pop() # indeks numarası belirtmezsek listenin son elemanını siler
print(a)
"""
del() metodu da aynı görevi görür.
fakat del metoduna indeks numarası 
vermezsek liste silinir.
"""

a.append(5)
a.remove(1) # listedeki silmek istediğimiz elemanı direk bu metoda yazmalıyız.
print(a)

a.insert(0, 100) # listede istediğimiz indekse eleman eklememizi sağlar.
print(a)

print(a.pop()) # listeden silinen elemanı yazdırır.
print(a)

a.clear() # bu metod listenin içeriğini siler.
print(a)