

# 1.  Kullanıcıya memleketini sorarak hemşeri olup olmadığınızı yazdıran programı yazınız.
"""
name_ = input("Adınızı Giriniz.: ")
city = input("doğduğunuz şehri giriniz.: ")
status = f"{name_} Hemşerim Merhaba" if city.lower() == "aydın" else f"{name_} Hemşeri değiliz." 
print(status)
"""

# 2.  Kullanıcıdan iki sayı isteyerek büyük olanı ve küçük olanı saırasıyla ekrana yazdıran uygulamayı yazınız.
"""
number1 = int(input("Birinci sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz:  "))
result = f"1. Sayı: {number1} İkinci sayı: {number2}" if number1 > number2 else f"1. Sayı: {number2} İkinci sayı: {number1}"
print(result)
"""

# 3.  Kullanıcıdan 3 adet sayı isteyerek sayıları büyükten küçüğe sırayla yazdırınız.
"""
number1 = int(input("Birinci sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz:  "))
number3 = int(input("Üçüncü sayıyı giriniz:  "))
if number1 == number2 and number2== number3 and number1 == number3:
    print("sayılar eşit")
else:
        
    if number1 == number2:
        print("Birinci sayı ikinci sayıya eşit")
        if number1 > number3:
            print(number1,number2,number3)
        else:
            print(number3,number1,number2)    
    elif number1 == number3:
        print("Birinci sayı Üçüncü sayıya eşit")
        if number1 > number2:
            print(number1,number3,number2)
        else:
            print(number2,number1,number3)
    elif number2 == number3:
        print("İkinci sayı üçüncü sayıya eşit")
        if number2 > number1:
            print(number2,number3,number1)
        else:
            print(number1,number2,number3)     

    if number1 > number2 and number1 > number3 :
        max_number1 = number1
        if number2 > number3:
            max_number2 = number2 
            print(max_number1, max_number2,number3)
        else:
            max_number2 = number3 
            print(max_number1, max_number2,number2)
    elif number2 > number1 and number2 > number3 :
        max_number1 = number2
        if number1 > number3:
            max_number2 = number1
            print(max_number1, max_number2,number3)
        else:
            max_number2 = number3 
            print(max_number1, max_number2,number1)
    elif number3 > number1 and number3 > number2 :
        max_number1 = number3
        if number1 > number2:
            max_number2 = number1
            print(max_number1, max_number2,number2)
        else:
            max_number2 = number2 
            print(max_number1, max_number2,number1)
"""
  
# 4.  küşüye ehliyet için gerekli yaş ve eğitim sorularını sararak ehliyet alma durumunu yazdırınız (eğitim için ilkenaz ilköğretim mezunu olması gerekmektedir)
"""
name_=input("Adınızı yazınız    : ")
age = int(input("Yaşınızı yazınız   : "))
if  age < 18 or age > 78 :
    print(name_," ehliyet almanız için 18 - 78 yaş aralığında olmalısınız. ")
else:
    print("1. Okul yok\n2. İlkokul\n3. Ortaokul\n4. Lise\n5. Lisans ve lisans üstü")
    education = int(input("Aldığınız eğitim sıra nosunu giriniz: "))
    if education <= 5 and education >=1:
        if education > 1 :
            print(name_,"Bir Direksiyon kursuna kayıt olunuz.")
        else:
            print(name_,"Ehliyet almak için en az ilk okul mezunu olmanız gerekiyor.")
    else:
        print("Seçiminiz Hatalı.")
"""

# 5.  Bir turnava düşünerek gerekli koşulları belirleyiniz. en az iki koşul olmak üzere kullanıcının turnuvaya katılıp katılmayacağı bilginizi veren programı yazınız.
"""
name_ = input("Adınızı yazınız      :")
tall = float(input("Boyunuzu cm cinsinden yazınız    :"))
weigth = float(input("Kilonuzu kg cinsinden yazınız :"))
resault = f"{name_} Turnuvaya Hoşgeldiniz" if tall >= 175 and weigth >= 65 else f"{name_} üzgünüz boy/kilo uygun değil"
print(resault)
"""

# 6.  bir menü sipariş kontol sistemi yazınız. müşterinin menüsünün doğru olup olmadığını kontrol ediniz.(bir yiyecek ve içecek olmalı)
"""
food = input("Yiyecek siparişinizi giriniz : ")
drink = input("İçecek siparişinizi yazınız  : ")
if (food.lower() == "pizza" or food.lower() == "hamburger") and (drink.lower() == "ayran" or drink.lower() == "çay"):
   print("Servis için Teşekkürler.")
else:
    print("hatalı sipariş")
    if food.lower() != "pizza" or food.lower() != "hamburger":
            print("Yanlış Yiyacek Servisi")
            if drink.lower() != "pizza" or drink.lower() != "hamburger":
                print("Yanlış İçecek Servisi")
    elif drink.lower() == "pizza" or drink.lower() == "hamburger":
        print("Yanlış İçecek Servisi")
"""

# 7.  Hergün bir farklı bir mahalleye gidecek olan pazarlama elemanının, haftanın hangi gününde hangi mahallede olacak olduğunu söyleyen bir program yazınız.(elifli yapı)
"""
print("\n1. Pazaretesi\n2. Salı\n3. Çarşamba\n4. Perşembe\n5. Cuma\n6. Cumartesi\n7. Pazar")
dayName = int(input("Gün sıra numarasını Giriniz :"))

if dayName ==1:
    print("Atatürk Mahellesi")
elif dayName ==2:
    print("Cumhuriyet Mahellesi")
elif dayName == 3:
    print("9Eylül Mahellesi")
elif dayName == 4:
    print("8Eylül Mahellesi")    
elif dayName == 5:
    print("Zafer Mahellesi")
elif dayName == 6:
        print("Merkez Mahellesi") 
elif dayName == 7:
    print("Kazımdirik Mahellesi")
else:
    print("Yanlış Seçim.") 
""" 
 #************** match case yapısını kullann*********
"""
match dayName:
   case 1:
       print("Atatürk Mahellesi")
   case 2:
       print("Cumhuriyet Mahellesi")
   case 3:
       print("9Eylül Mahellesi")
   case 4:
        print("8Eylül Mahellesi")
   case 5:
        print("Zafer Mahellesi")
   case 6:
        print("Merkez Mahellesi")
   case 7:
        print("Kazımdirik Mahellesi")
   case _:
       print("yanlıs seçim")
"""
       
# 8.  Kullanıcıdan üç adet oratalama isteyerek ders gerçeme durumunu yazdıran programı yazınız.

"""
point1 = float(input("Birinci Notu Giriniz : "))
point2 = float(input("İkinci Notu Giriniz : "))
point3 = float(input("Üçüncü Notu Giriniz : "))
finalPoint = (point1 + point2 + point3) / 3

resualt = "geçti" if finalPoint >= 50 else "Kaldı"
print(resualt,"Puanınız: ", finalPoint) 
"""
# 9.  Yukarıda ki soruya devam drumunu da ekleyerek geçme kalma durumunu belirtiniz.
"""
point1 = float(input("Birinci Notu Giriniz : "))
point2 = float(input("İkinci Notu Giriniz : "))
point3 = float(input("Üçüncü Notu Giriniz : "))
finalPoint = (point1 + point2 + point3) / 3
attendance = int(input("Devam durumunuzu yazınız. (1 devamsızlık yok, 0 devamsız.)"))
resualt = "geçti" if finalPoint >= 50 and attendance ==1 else "Kaldı"
print(resualt,"Puanınız: ", finalPoint) 
"""

# 10. Kullanıcı adı ve şifre isteyerek doğru bilgileri girmesi halinde kullanıcıya hoşgeldin mesajı veren uygulamayı yazınız.
"""
passwordDefault = "python963"
userNameDefault = "python"
password_ = input("Parolanızı Giriniz  : ")
userName = input("Kullanıcı Adını Giriniz: ")
resault = f"{userName} Hoşgeldiniz" if password_ == passwordDefault and userName == userNameDefault else "Yanlış parola/kullamıcı adı."
print(resault)
"""

# 11. Kullanıcının geçerli bir mail adresi girip girmediğini denetleyen bir program yazınız. (@ karakterinin varlığını kontrol ediniz)
"""
email = input("emailiniz giriniz : ")
resault = "emailiniz kaydedildi" if  "@" in email else "email formatınız uygun değil"
print(resault)
"""

# 12. Kullanıcıya sevdiği programlama dilini sorarak, o programlama dilini geliştiren kişi(leri)n ismini yazıran programı yazınız. 4 adet yeterli
print("\n1. python \n2. C# \n3. SQL \n4. Java")
"""
number = int(input("Sevdiğiniz Programa dilinin sıra numarasını giriniz.: "))
match number:
    case 1:
        print("Şahin EROL - Python")
    case 2:
        print("Şahin EROL - C#")
    case 3:
        print("Şahin EROL - SQL")
    case 4:
        print("Şahin EROL - Java")
    case _:
        print("Seçanek dışı.")    
"""    
    
# 13. Kullanıcıya seçtiği menüye göre fiyat bilgisi veren restoran uygulamasını yazınız.
"""
menu1 = 300
menu2 = 350
print("\n1. Hamburger, Salata, Çay\n2. Tavuk, Pilav, Ayran")
menu = int(input("menüden sıra numarasına göre bir menu seçiniz."))
match menu:
    case 1:
        print("Hamburger, Salata, Çay:", menu1)
    case 2:
        print("Tavuk, Pilav, Ayran:", menu2)
    case _:
        print("Bir menu seçmelisiniz.")
"""

