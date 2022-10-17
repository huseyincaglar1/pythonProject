#python dilinde değişken tanımlarken veri tipini yazmamıza ihtiyaç yoktur.
#Çünkü python bu işi bizim için yapıyor.

kelime = "Python"
print(type(kelime))

kelime2='Python2'
print(type(kelime2))
#tek tırnak ve çift tırnak kullanmak arasında bir fark yoktur.

sayi = 523456789034567812345678798654322456785423232456432
#python büyük sayı yazımında bir sorun teşkil etmez. İşlemler yapılabilir.
print(type(sayi))

ondalikli_sayi = 3.6
print(type(ondalikli_sayi))

negatif_sayi = -124523612345678
print(type(negatif_sayi))

hiclik = None
print(type(hiclik))

boolean = True
print(type(boolean))

print(sayi,ondalikli_sayi,negatif_sayi,sep="//")
#sep komutunun içine ne koyarsan parametrelerin arasına onu koyar.

print(hiclik,boolean,end="--")
print("aynı satırdan devam")
#end komutu aynı satırdan yazdırmaya devam ettirir.

print(sayi); print(hiclik); print(boolean)
#deyimlerimizi aynı satıra yazmak istersek ifadelerin arasında noktalı virgül kullanmak şapşart!!!
#deyimlerimizi aynı satıra yazdık diye çıktımız aynı satırda olmayacak tabiki de:)

sayi2,kelime3,boolean2 = 2,"merhaba",True
print(sayi2,kelime3,boolean2)
#farklı veri tiplerini bile beraber tanımlayabilip yazdırabiliyoruz.

"""
3 tane çift tırnak arası yorum satırı olur.
"""

'''
3 tane tek tırnak da aynı görevi görür.
'''

liste = [1, 2]

a = None; d = 7

sozluk = {a: "wer", d: "df"}

degistirilmeyen_liste= (1, 3.6, "kelime")
#tuple liste ancak başka liste türüne çevrilirse değişim yapılır.
#farklı veri tiplerini içinde barındırabilir.
"""
a = list(degistirilmeyen_liste)
a[2] = 7 #Bu şekilde tuple listede güncelleme yapılabilir.
degistirilmeyen_liste = tuple(a)
"""
print("liste :", type(liste))
print("i :", type(sozluk))
print("değiştirilmeyen liste :", type(degistirilmeyen_liste))


h = 7
H = 16 #değişken tanımlamada büyük ve küçük harfin önemi vardır.
print(h, H, sep=" : ")