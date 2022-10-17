a = 5
def b():
    a = 10
    print(a)
#fonksiyon içindeki değer fonksiyonun içinde kalır.

b()
print(a)

def c():
    global a
    a = 10
    print(a)
#global komutu a değişkenini evrensel yaparak fonksiyonun dışındaki değerin değişmesini sağlıyor.

c()
print(a)


