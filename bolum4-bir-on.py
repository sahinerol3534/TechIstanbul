#  1. 1-30 arasındaki tek sayıları yazdıran programı yazınız
"""
print("1 den 30 a kadar tek sayılar")
for i in range(1,30,2):
    print(i, end = " ")
print()
"""

#  2. Girilen 10 Sayının Toplamını ve ortalamasını Bulan programı yazınız.
"""
i = 1
total = 0
while i <= 10:
    number = int(input(f"{i}. sayıyı giriniz.: "))
    total += number
    i += 1
average = total / (i - 1)
print(f"toplamı {total} olan {i-1} adet sayının ortalaması: {average} ")
"""

#  3. Python 50’den 20(dahil ise)’ye kadar olan sayıları 3’er azaltarak ile ekrana yazdırınız.
"""
print("50 den 20 ye 3 er azalan sayılar")
for i in range(50, 17, -3):
    print(i, end = " ")
print()
"""

#  4. Girilen 20 sayıdan Tek ve Çift Sayıların Ortalamasını Hesaplattırarak ekrana yazdıran uygulamayı yazınız.
"""
i = 1
even = odd = 0

totalOdd = totalEven = 0
while i <= 20:
    number = float(input(f"{i}. sayıyı giriniz.: "))
    if number %2 == 0:
        totalEven += number
        even += 1
    else:
        totalOdd += number
        odd += 1
    i +=1
if odd == 0:
    print("Girmiş olduğunuz sayıların hepsi çift sayı") 
    averageEven = totalEven / even 
    print(f"{i-1} adet sayıdan {even} tanesi çift, çift sayılar toplamı: {totalEven}, çift sayılar ortalaması: {averageEven}")
 
elif even == 0:
    print("Girmiş olduğunuz sayıların hepsi tek sayı sayı") 
    averageOdd = totalOdd / odd  
    print(f"{i-1} adet sayıdan {odd} tanesi tek, tek sayılar toplamı: {totalOdd}, tek sayılar ortalaması: {averageOdd}")
"""

#  5. Python ile iç içe For Döngüsü kullanarak 1′ den 10′ akadar çarpım tablosu oluşturunuz. (Yanyana çıktı veren versiyonunuda deneyiniz)
"""
for n in range (1,11):
    print(f"***** {n} *****  ",  end = " ")
print()
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{j :> 2} x {i :>2} = {(i * j):>3}",  end = "   ")
    print()
"""

#  6. Python ile iç içe while kullanarak 1′ den 10′ akadar çarpım tablosu oluşturunuz. (Yanyana çıktı veren versiyonunuda deneyiniz)
"""
for n in range (1,11):
    print(f"***** {n} *****  ",  end = " ")
print()

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{j :> 2} x {i :>2} = {(i * j):>3}",  end = "   ")
        j += 1
    i +=1
    print()
"""

#  7. Kullanıcıdan 2 kez aynı parolayı girmesini isteyerek, iki defa aynı parola girildiğinde giriş yapan farklı girildiğinde uyaran kodları oluşturun?
"""
password1 = input("Parolanızı giriniz: ")
password2 = input("Parolanızı tekrar giriniz: ")  
result = "Giriş Başarılı Hoş Geldiniz." if password1 == password2 else "Parolalar uyuşmuyor. Tekrar deneyiniz."
print(result)
"""
#  8. Python 100'e kadar 3'e ve 5'e Tam Bölünen Sayıları Listeleyen Örnek yazınız
"""
number = number1 = number2 = 0
for i in range(1, 101):
    if i %3 == 0:
        number +=1
        print(f"{i} --> 3'e bölünen ")
        
    elif i %5  == 0:
        number1+=1
        print(f"{i}  --> 5'e bölünen ")
print(f"3' e bölünen {number} adet")
print(f"5' e bölünen {number1} adet") 
for j in range(1,101):
    if j %3  == 0 and j % 5 == 0:
       number2 +=1
       print(f"{j} hem 3'e hemde 5'e bölünen ")   
print(f"hem 3'e hemde 5'e bölünen {number2} adet")
"""

#  9. "" kullanarak 44 bir kare olşturunuz.
"""
for i in range(4):
    for j in range(4):
        print("*", end = " ")
    print()
"""

# 10. "*" kullanarak kullanıcının belirlediği ölçülerde bir dikdörtgen oluşturunuz.
number1 = int(input("oluşturmak istediğiniz kısa kenar * sayısını giriniz: "))
number2 = int(input("oluşturmak istediğiniz uzun kenar * sayısını giriniz: "))
"""
for i in range(number1):
    for j in range(number2):
        print("*", end = " ")
    print()
"""

for i in range(number1):
  print((number2 * "* "), )
    