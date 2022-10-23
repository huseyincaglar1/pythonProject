class sinif:
    a = 0
    b = "ads"
    c = [1, 3, 5]

    def yazdir(self):
        d = 100
        print(d, self.a)

    def yazdir2(self, t):
        self.yazdir()
        print(t)

nesne = sinif()
print(type(nesne))

nesne.yazdir()
print(nesne.a)

nesne.a = 999
print(nesne.a)
nesne.yazdir()

nesne.yazdir2("string")
