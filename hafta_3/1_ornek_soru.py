"""
kendisine gönderilen sayılardan sadece palindrom
olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.
"""

def fonksiyon(*polindram):
    toplam = 0
    for sayi in polindram:
        if  str(sayi) == str(sayi)[::-1]:
            toplam+=sayi
        else:
            toplam-=sayi
    return toplam
print(fonksiyon(22,35,555,9889,1234))