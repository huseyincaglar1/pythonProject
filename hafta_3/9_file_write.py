dosya = open("cop.txt", 'w')
print("cop adli dosyaya bu yaziyi yazdiriyorum", file=dosya)
print("altina da bunu yaziyorum", file=dosya)
dosya.close()

dosya = open("kod.txt", 'w')
print("print('efsane python')", file=dosya)
dosya.close()

dosya = open("kod.txt", 'r')
satir = dosya.readline()
eval(satir)