def yazdir():
    print("Yazıyorum")

yazdir()

def topla(a, b):
    return a+b

print(topla(3, 5))
#parametrik fonksiyon

def topla_carp(a, b, c):
    return a + b + c, a * b * c

toplam, carpim = topla_carp(3, 5, 2)
print(topla_carp(3, 5, 2))
print(toplam, carpim,sep="\n")
#iki değer döndürme

def topla_ne_varsa_git(*a):
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam

print(topla_ne_varsa_git(3, 5, 9, 15.2, 36))
#birden fazla değer döndürme




