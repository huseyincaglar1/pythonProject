a = [1, 2, 3, 4, 5]
b = [True, 5.8, 9879545454, None, [1, "ad", 8.5]]

print(a)
print(b)
print(b[0]) # b listesinin 0. indeksteki elemanını yazdırır.
print(b[4][1]) # b listesinin 4. indeksteki elemanının 1. indeksteki elemanını yazdırır.

tr = "Türkiye"
print(tr[1:4]) # tr stringindeki 1. ve 4. indeksteki elemanlar arasını yazdırır.(4. elemanı saymaz)

b[4][1] = [6, 99, 6.5, "zasas"] # burada b listesinin elemanının elemanı değiştiriliyor.
print(b[4][1])
print(b[4][1][3]) # iç içe listeler olabiliyor.
