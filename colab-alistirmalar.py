

   # 1. Bir öğrencinin matematik dersinden aldığı notlar sırasıyla 64, 86 ve 70’tir. Bu öğrencinin not ortalamasını hesaplayınız.
"""
exam_point1 = 64
exam_point2 = 86
exam_point3 = 70
result = (64+86+70)/3
print("not ortalamasi:", result)
"""

   # 2. Kullanıcıdan adını ve yaşını alarak adını yaşı kadar yazdıran programı yazınız.
"""
name = input("adınızı yazınız: ")
age = int(input("yaşınızı yazınız: "))
print(age * (name))
"""

   # 3. Dairenin alanını ve çevrenisi hesaplayan bir progrm yazınız. Pi değerini ve yarı çap değerini kullanıcıdan alınız.
"""
diameter = float(input("Dairenin çapını giriniz: ")) 
number_pi = float(input("Hesaplamalarda kullanacağınız pi sayısını giriniz: "))
area = diameter **2 / 4 * number_pi
primeter = diameter * number_pi
print("Dairenin alanı:      ",area)
print("Dairenin çevresi:    ", primeter)
"""
   
   # 4. Kullanıcıdan doğum tarihini isteyerek ehliyet alma durumunu belirten programı yazınız.
"""
name = input("Adınızı giriniz:     ")
birth_date = int(input("Doğum tarihinizi (yyyy) yıl olarak giriniz: "))
age = 2025 -birth_date

if age < 18:
    print(f"{name} {age} yaşındasınız. Ehliyet almak için 18 yaşında olmanız gerekiyor.")
else:
    print(f"{name} {age} yaşındasınız. Gerekli evrakları tamamlayarak sürücü kursuna baş vurunuz.")

    # veya
status = (f"{name} {age} yaşındasınız. Ehliyet almak için 18 yaşında olmanız gerekiyor.") if age < 18 else (f"{name} {age} yaşındasınız. Gerekli evrakları tamamlayarak sürücü kursuna baş vurunuz.")

print(status)
"""
   # 5. Kullanıcıdan faiz oranı ve para miktarını öğrenerek, girilen paranın yıllık faizini hesaplayan programı yazınız.
"""
amount = float(input("Ana para tutarını giriniz.:                       "))
rate = float(input("Yıllık ('0,' olmadan 'ff.ff' gibi) faizi oranını giriniz.   "))
interest = amount * rate / 100
total = amount + interest
print("Anapara      :",amount)
print("Yıllık faiz  :",interest)
print("Yıl sonu toplam miktar:",total)
"""

   # 6. Kullanıcıdan alacak olduğunuz veriler ile kullanıcının vücud kitle endeksini hesaplayan programı yazınız.
"""
name = input("Adınızı giriniz.:     ")
tall = float(input("Boyunuzu cm olarak giriniz.: "))
weigth = float(input("Kilonuzu kg olarak giriniz.: "))
boddyMassIndex = weigth /((tall/100)**2)
if boddyMassIndex < 18.5:
    print(f"{name} vücut kitle indeksiniz: {boddyMassIndex} Durumunuz: ZAYIF")
elif 18.5 <= boddyMassIndex < 25:
    print(f"{name} vücut kitle indeksiniz: {boddyMassIndex} Durumunuz: NORMAL")
elif 25 <= boddyMassIndex < 30:
    print(f"{name} vücut kitle indeksiniz: {boddyMassIndex} Durumunuz: FAZLA KİLOLU")
else:
    print(f"{name} vücut kitle indeksiniz: {boddyMassIndex} Durumunuz: OBEZ")
"""

   # 7. kullanıcının sizinle adaş olup olmadığını yazdıran programı yazınız.
"""
name = input("Adınızı giriniz: ")
status = "Adaşız" if name.lower() == "şahin" else "Adaş değiliz." #Not: türkçe dil ayarı yapılmalı.
print(status)
"""

   # 8. Kullanıcıdan not ortalamasını isteyerek teşekkür, tadir alıp alamama durumunu yazdıran programı yazınız.
"""
name = input("Adınızı giriniz   : ")
average_grade = float(input("Not ortalamanızı giriniz.: "))
if average_grade < 80:
    print(f"{name} Ne yazık ki bir belge almaya hak kazanmadınız.")
elif 80 <= average_grade < 90 :
    print(f"{name} Tebrikler TEŞEKKÜR belgesi almaya hak kazandınız.")
elif average_grade >= 90 :
    print(f"{name} Tebrikler TAKDİR belgesi almaya hak kazandınız.")
else:
    print("Yanlış giriş yaptınız.")
"""
    
   # 9. Kullanıcıdan otoban uzunluğunu ve geçiş süresini isteyerek hızınız hesaplayınız. daha sonra kullanıcının hız cezası alıp almama durumunu yazdırınız.
"""distance_ = float(input("Katettiğiniz mesafeyi km cinsinden giriniz.: "))
time_ = float(input("Seyahat süresini saat cinsinden giriniz.: "))
speed = distance_ / time_
print("Hızınız:", speed,"km/saat")
"""

   # 10. Yevmiyesi 350 TL olan bir işçinin çalışma gün sayısını öğrenerek, yevmiye tutarıı hesaplayan programı yazınız.

"""
workday = float(input("Çalıştığınız gün sayısını yazınız: "))
print("Hakedilen Ücret: ",(350*workday),"TL")
"""
