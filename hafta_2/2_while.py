a = 5
while a < 15:
    a += 2
    if a == 10:
        continue
    if a == 12:
        break # a 12 ye eşit olursa döngü sonlanır.
        #break ifadesi içinde bulunduğu döngüyü sonlandırır.
    print(a)
else:
    print("a 12 ye eşitlenmeden döngü biterse bu çalışır")
print(a)
