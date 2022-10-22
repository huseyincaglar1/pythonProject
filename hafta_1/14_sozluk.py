sozluk = {
  "marka": "Ford",
  "model": "Mustang",
  "yil": 1964
}

print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yil"])

"""
print(sozluk.get("marka"))
print(sozluk.get("model")) # bu şekilde de yazılabilir.
print(sozluk.get("yil"))
"""

sozluk["renk"] = "siyah" # eleman ekliyor.
print(sozluk)
print(sozluk["renk"])
sozluk["renk"] = "beyaz" # elemanın değerini değiştiriyor.
print(sozluk)

print(sozluk.keys())
print(sozluk.values())

for i in sozluk.keys():
    print(i, ":", sozluk[i])
"""
iki şekilde de yazdırılabilir.
"""
for a,b in sozluk.items():
   print(a,":",b)
