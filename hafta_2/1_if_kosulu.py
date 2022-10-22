a = 3
b = 7
c = 4

if b > a:
    print("b a dan büyüktür")
else:
    print("b a dan büyük değildir.")


if c < 0: print("c 0 dan küçüktür")
elif c > 0: print("c 0 dan büyüktür")
else: print("c 0 a eşittir")

print("a b den küçüktür") if a < b else print("a b den büyüktür")
#kısa if koşul ifadesinin yazımı

if b > c or b > a:
    print("b c den büyük veya b a dan büyüktür")
    # herhangi biri doğru ise çalışır
if c > a and b > a:
    print("c a dan büyüktür ve b a dan büyüktür")
    # iki ifade de doğru ise çalışır


if a is 3:
    print("a 3 e eşittir.")
if a is not 3:
    print("a 3 e eşit değildir")

if a is 3:
    if a > c or a < b:
        print("başarılı")
#iç içe if koşul ifadesinin kullanımı

if a > 2:
    pass
else:print("a 2 den büyük değildir.")
#Pass deyimi yürütüldüğünde hiçbir şey olmaz
#ancak boş koda izin verilmediğinde hata almayız.