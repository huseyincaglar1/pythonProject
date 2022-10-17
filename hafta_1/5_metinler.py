a = "merhaba"
b = """mer
ha
ba"""
print(a)
print(b)
print(a[0])
print(a[1])
print(b[3]) # b değişkenindeki boşluklar da sayılıyor.
print(b[6]) # bu değer boşluğa denk geldiği için çıktı boş görünecektir.

print("a nın uzuluğu :", len(a))#len komutu metin uzunluğunu bulur.
print("b nin uzuluğu :", len(b))

