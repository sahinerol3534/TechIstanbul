import random
    # 11. iç içe döngüler kullanarak piramit belirlediğiniz yükseklikte pramitler oluşturunuz. Örnek kod aşağıda vardır.
"""
satir=10
print('\n...Python Yıldızı...\n')
for i in range(satir):
    print(' '*(satir-i-1) + '*'*(2*i+1))


high = int(input("Piramit yüksekliğinini belirten sayı giriniz.:"))
for i in range(high):
    print(i, " " * (high-i-1) + "*" * (2 * i + 1))
"""
    # 12. Break deyiminin kullanımı görmek açısından 1'den 100' e kadar sayıları ekrana yazdırırken, her sayıyı kontrol edelim ve eğer sayı 35 ise döngüden çıkalım.
"""
for i in range(100):
    print(i)
    if i == 35:
        break
"""
    # 13. Şimdi kullanıcıya bir sayı girmesini isteyelim ve break komutu kullanarak 1den kullanıcının girdiği sayıya kadar olan sayıları ekrana yazdıralım.while ile sonsuz döngü oluşturunuz.
"""
number = int(input("bir sayı giriniz. : "))
i = 1
while True:
    
    if i == number-1:
        print("",end ="")
    if i == number:
        
        print(i," --> Girdiğiniz sayıya geldik.")
        break
    print(i)
    i +=1
"""

    # 14. Birlikte sayı bulmaca yapalım. sayimiz isimli bir değişken tanımlayıp, 1 ile 100 arasında istediğimiz bir sayıyı o değişkene atayalım. Ve kullanıcıya bir sayı girmesini isteyelim. Kullanıcı tuttuğumuz sayıyı yanlış girdiğinde "Yanlış, Bir kez daha dene!" mesajını ekrana yazdıralım. Doğru sayıyı girdiğinde ise ekrana "Tebrikler Kazandınız" şeklinde bir uyarı mesajı yazdıralım.
"""
i = 1
random_number = random.randint(1, 100)
while True:
    
    myNumber = int(input("bilgisayarın tuttuğu sayıyı tahmin ediniz.: "))
    
    if myNumber == random_number:
        print(f"Doğru Tahmin. Kazandınız.!!! {i}.tahmin")
        break
    else:
        print("Birkez daha deneyiniz.!!!")
    i += 1
"""
    # 15. yukarıdaki örneği yönlendirme ile yaptırınız. (daha büyük sayı giriniz veya daha küçük sayı giriniz şeklinde)
"""
i = 1
random_number = random.randint(1, 100)
while True:
    myNumber = int(input("bilgisayarın tuttuğu sayıyı tahmin ediniz.: "))
    
    if myNumber == random_number:
        print(f"Doğru Tahmin. Kazandınız.!!! {i}.tahmin")

        break
    elif myNumber > random_number:
        print("Yüksek Tahmin Daha küçük bir sayı Tahmin ediniz.")

    else:
        print("Düşük Tahmin Daha büyük bir sayı Tahmin ediniz.")
    i += 1

"""

    # 16. Python 100'e kadar 3'e ve 5'e Tam Bölünen Sayılar harici sayıları Listeleyen Örnek yazınız
"""
for i in range(100):
    if i %3 != 0 and i  %5 != 0:
        print(i, end = " ")
print()
"""    

    # 17. Kullanıcıdan 10 sayı girmesini ve girilen sayıların faktöriyel değerlerini toplamasını isteyiniz. 
    #     negatif bir sayı girildiğinde sayı isteme işlemini bitirerek girilen toplam sayı adetini ve 
    #     elde edilen toplamı kullanıcıya yazdırırken, 7 ve katları sayılar girildiğinde gerekli hesaplamaları yapmayarak 
    #     devam eden uygulamayı yazınız.
"""
totalFac = 0
count_ = 0
for i in range(1, 11):
    number = int(input(f"{i}.sayıyı giriniz.: "))
    if number < 0:
        print("Pozitif bir sayı giriniz.: ") 
        break

    if number %7 == 0:
        continue
    
    factorial_ = j = 1
    while j <= number:
        factorial_ *= j
        j +=1

    print(factorial_)
    totalFac += factorial_
    count_ += 1
    print(totalFac)
     
print(f"{count_} adet sayı girdiniz.")
print(totalFac)
"""        

    # 18. Girilen iki sayının ebob ve ekok değerlerini bulup yazdıran programı yazınız.
"""
number1 = int(input("birinci sayıyı giriniz.: "))
number2 = int(input("ikinci sayıyı giriniz.: "))
limit = number1 if number1 < number2 else number2

ebob = 1
for i in range(1, limit + 1):
        if number1 %i == 0 and number2 %i == 0:
            ebob = i
print("ebob: ",ebob)

ekok = (number1 * number2) / (ebob)
print("ekok: ", ekok)
"""

    # 19. Python ile girilen sayının basamak sayısını bulan kodu yazınız.
"""
number = number1 = int(input("Bir tam sayı giriniz: "))
i = 1
b = 1
while True:
    number /= 10
   
    if number > 1:
        b += 1
    else:
        break
    i += 1
print("basamak sayısı.: ", b)
print("-------------------------------")
"""
# ------------------------refaktör -------------------------------------

"""
number = number1 = int(input("Bir tam sayı giriniz: "))
temp =number
basamak_sayisi = 0
while temp > 0:
    temp //= 10
    basamak_sayisi += 1
print("Basamak Sayısı.: ", basamak_sayisi)
print()

print("***** Basamaktaki Sayılar *****")

temp = number
while temp > 0:
    rakam = temp %10 
    print(rakam, end = ", ")
    temp //= 10
print()
print("\n****************************")
temp = number
while basamak_sayisi > 0:
    bolen = 10 ** (basamak_sayisi - 1)
    rakam = temp // bolen
    print(rakam, end = ", ")
    temp = temp % bolen
    basamak_sayisi -= 1
print()
"""


    # 20. Bir sayının, tüm basamaklarındaki rakamların sayının basamak katına toplamı kendisine eşit olan sayılara 
    # Armstrong sayısı denir. Örneğin; 407 sayısını ele alalım. 407’yi rakamlarına ayıralım. 
    # Sonrasında da bu rakamları, sayı üç haneli olduğu için rakamların küplerini alıp toplayalım:
    #     407 ➡️ (43) + (03) + (73) = 407 yapmaktadır. Yani bu demektir ki 407 sayısı Armstrong bir sayıdır. 
    # Şimdi bunu Python ile kodlayınız. 
"""
number = int(input("Bir tam sayı giriniz.: "))
temp = number 
basamak_sayisi = 0
while temp > 0:
    temp //= 10
    basamak_sayisi += 1
print("Basamak Sayısı.: ", basamak_sayisi)

temp = number
ust = basamak_sayisi
basamakSayiToplami = 0
while basamak_sayisi > 0 :
    bolen = 10 ** (basamak_sayisi-1)
    rakam = temp // bolen
    basamakSayiToplami += (rakam ** ust )
    temp %= bolen 
    basamak_sayisi -= 1
print(basamakSayiToplami)
if basamakSayiToplami == number:
    print("Girdiğiniz sayı bir Amstrong Sayısıdır.")
"""
    # 21. 1000'e kadar olan Armstrong sayılarını yazdırınız. 
"""for number in range(1001):
    temp = number 
    basamak_sayisi = 0
    while temp > 0:
        temp //= 10
        basamak_sayisi += 1
    if number == 0:
        basamak_sayisi = 1

    temp = number
    ust = basamak_sayisi
    basamakSayiToplami = 0
    while basamak_sayisi > 0 :
        bolen = 10 ** (basamak_sayisi-1)
        rakam = temp // bolen
        basamakSayiToplami += (rakam ** ust )
        temp %= bolen 
        basamak_sayisi -= 1
    
    if basamakSayiToplami == number:
        print(basamakSayiToplami," Amstrong Sayısıdır.")
"""

    # 22. kullanıcıya 10 hak vererek Armstrong sayısını oluşturup oluşturamadığını test ediniz.
"""bilmeSayisi = 0
for i in range(1,11):
    number = int(input("Bir tam sayı giriniz.: "))
    temp = number 
    basamak_sayisi = 0
    while temp > 0:
        temp //= 10
        basamak_sayisi += 1
    if number == 0:
        basamak_sayisi = 1

    temp = number
    ust = basamak_sayisi
    basamakSayiToplami = 0
    while basamak_sayisi > 0 :
        bolen = 10 ** (basamak_sayisi-1)
        rakam = temp // bolen
        basamakSayiToplami += (rakam ** ust )
        temp %= bolen 
        basamak_sayisi -= 1
    
    if basamakSayiToplami == number:
        bilmeSayisi += 1
        print(basamakSayiToplami," Girdiğiniz sayı bir Amstrong Sayısıdır. toplam ", bilmeSayisi,"adet bildiniz",10 - i, "hakkınız kaldı.")

    else:
        print(f"Girdiğiniz sayı bir Amstrong sayısı değil {10 - i} hakkınız kaldı.")
"""
