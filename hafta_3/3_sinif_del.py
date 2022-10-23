class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
    """
    Class içinden türetilen nesnelere ait 
    özellikler bu metot ile nesnelere atanır.
    Eğer bir class'tan nesne türetecek isek __init__
    class'ın ilk metodu olmak zorundadır.
    """

    def __del__(self):
        print("beni siliyorlar...")


nesne = sinif("Merhaba")
print(nesne.metin)
del nesne