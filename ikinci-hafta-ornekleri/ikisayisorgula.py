x = int(input("Birinci Sayı: "))
y = int(input("İkinci Sayı: "))

if x > y:
    print("Birinci sayı, ikinci sayıdan büyüktür.")
else:
    if y > x:
        print("İkinci sayı birinci sayıdan büyüktür.")
    else:
        print("İki sayı birbirine eşittir.")
