dosya = open("metin.txt", "r")

oku = dosya.read(6)
print(oku)
#dosyanın parantez içine yazdığımız kadar karakterini okur.

print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
#her print sırasıyla sadece bir satır yazdırır.

for satir in dosya:
    print(satir)
#readline ile aynı görevi görür.
#tabi bunun yazımı daha basit:)
