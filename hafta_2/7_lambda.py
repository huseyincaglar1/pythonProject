lambda_fonksiyonu = lambda a: a + 10

print(lambda_fonksiyonu(5))
# lambda tek satırlık fonksiyondur.

islem_1 = lambda a, b, c: a + b * c

def islem_2(a, b, c):
    return a + b * c

print(islem_1(3, 5, 2))
print(islem_2(3, 5, 2))
print(type(islem_1))
print(type(islem_2))
#çok parametreli lambda

def islem(n):
  return lambda a : a ** n

kare_al = islem(2)
kup_al = islem(3)

print(kare_al(4))
print(kup_al(4))
#burada lambda fonksiyonunu hem kare almak hem de küp almak için kullandık.