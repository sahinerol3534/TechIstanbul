# 1. print() fonksiyonun görevini açıklayınız.
print("\n1. print() fonksiyonu konsola seçilen parametreyi yazdırmak için kullanılır.")
# 2. Kendizi tanıtan bir python programı yazınız. (En az 5 satır çıktı vermelidir)
print("\n2. ---- KİŞİSEL TANITIM KARTI ----")
print(" İsim    :","Şahin EROL")
print(" Yaş     :",66)
print(" Şehir   :","İstanbul")
print(" Hobi    :","Balık Tutmak")

# 3. Yorum satırlar (Comment Line) nedir? hangi amaçlarla kullanılır? Kaç farklı şekilde yorum satırı yazılabilir örneklerle açıklayınız
print("\n3. Yorum satırı program derlenirken derleyicinin dikkate almadığı satırlardır.\nYazılan kod için açıklamalar, uyarılar barındırır.")
# 4. yorum satılarının ne olduğu konusunda çıktı veren ve yorum satırı barındıran bir program yazınız.

print("\n4. ",9 == 5)  # false döner
print("9" == "5") #false  döner 
print("sonuç olarak int ler str gibi algılanır diyebilir miyiz?")
# 5. Pythonda kullanılan temel veri tipleri nelerdir ? ilkel veri tipi olarakta adlandırılan bu veri tiplerini yorum satırları içeren bir programla örnek içerecek şekilde yazınız.
print("\n5. ",1, "int---->","#tam sayı veri")
print(" . ",1.0, "float---->","#ondalık sayı veri")
print(" . ","techİstanbul", "string---->","#sözel veri")
print(" . ","1 - 0 veya True - False", "boolen---->","#olumlu veya olumsuz karar tipi veri")
# 6. type() fonksiyonunun görevini açıklayınız. type() fonksiyonu içerecek şekilde bir örnek yazınız.
print("\n6. type() fonksiyonu veri tipini döndürür. Örnek:")
print(type(1),"  ",type(1.0),"  ",type("1.0"),"  ",type(True),"  ",type(False))
# 7. Değişken nedir? Hangi amaçla kullanılır? Değişken tanımlarken dikkat edilmesi gereken unsurları belirtiniz.
print("\n7. Değişken kendilerine değer atadığımız yapılardır.")
print(" . değişken adı:","\n   .Bir sayı ile başlayamaz. ", "\n   .Türkçe karakter kullanılmaması tercih edilir. ",
     "\n   .programda kullanılan rezerv kelimeler olamaz input, print vb. ","\n   .Arada boşluk bırakılamaz. ",
     "\n   .Alt çigi ile başlayabilir. ","\n   .Başta olmamak kaydıyla sayı içerebilir, ",
     "\n   .Büyük küçük harf duyarlılığı vardır örneğin: ad, AD, aD, Ad farklı değişkenlerdir.",
     "\n   .Anlamlı olması tercih edilir.")

# 8. Farklı veri tiplerine sahip değişkenler tanımlayarak bir program yazınız.
ad_soyad = "Şahin EROL"
yas = 66
sehir = "İstanbul"
hobi = "Seyahat Etmek"
boy = 1.75
devam_durumu = True

print("\n---- KİŞİSEL TANITIM KARTI ----")
print(" İsim    :",ad_soyad,"      --->", type(ad_soyad))
print(" Yaş     :",yas,"              --->", type(yas))
print(" Şehir   :",sehir,"        --->", type(sehir))
print(" Hobi    :",hobi,"   --->", type(hobi))
print(" Boy     :",boy,"            --->", type(boy))
print(" Devam Durumu:",devam_durumu,"        --->", type(devam_durumu))
# 9. Kendinizi tanıtan farklı veri tiplerine sahip verilerden oluşacak şekilde bir program yazınız.
ad_soyad = "Şahin EROL"
yas = 66
sehir = "İstanbul"
hobi = "Seyahat Etmek"
boy = 1.75
devam_durumu = True

print("\n---- KİŞİSEL TANITIM KARTI ----")
print(" İsim    :",ad_soyad)
print(" Yaş     :",yas)
print(" Şehir   :",sehir)
print(" Hobi    :",hobi)
print(" boy     :",boy,"m")
print(" Devam Durumu:",devam_durumu)
# 10. Çoklu değişken ataması nasıl yapılır örnek içeren bir program yazınız.
adi, soyadi,yasi,boyu = "Şahin","EROL",66,1.75
print("\n10. Adı Soyadı :", adi+" "+soyadi,
      "\n    Yaş        :", yasi,"\n    boyu       :",boyu,"m")