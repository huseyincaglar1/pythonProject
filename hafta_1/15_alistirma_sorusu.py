"""
1 - Klavyeden girilen 6 tane sayıyı bir listeye atarak
    bunların karelerinden 30 çıkartıp mutlak değerini ortaya çıkan sonuca
    göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
"""
liste = []
for i in range(6):
    liste.append(eval(input()))


def siralama_fonksiyonu(a):
    return abs(a * a - 30)


liste.sort(key=siralama_fonksiyonu)
print(liste)





