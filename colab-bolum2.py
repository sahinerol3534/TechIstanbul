
    # 1. Kullanıcıdan veri almak için kullanılan fonksiyon nedir?
firstName = input("Adınızı giriniz:     ")
lastName = input("Soyadınızı giriniz:     ")
age = int(input("Yaşınızı giriniz:  "))
tall = float(input("Boyunuzu giriniz:  "))

    # 2. Kullanıcıdan cevap alabileceğiniz basit bir tnışma programı yazınız.
hoby = input("Hobinizi giriniz:   ")
print("*****************************************")
print(f"\nMerhaba {firstName} {lastName} Bootcampımıza hoşgeldiniz.")
print(f"\nAdınız: {firstName} \nSoyadınız: {lastName} \nYaşınız: {age} \nBoyunuz: {tall} \nHobiniz: {hoby}")

    # 3. ilkel - temel veri tipleri arasında dönüşüm yapmak için kullanılan fonksiyonlar nelerdir?
number = "8"
type1 = type(number)
number1 = int(number) 
type2 = type(number1)
number2 = 8
type3 = type(number2)
number2_1 = str(number2)
type4 = type(number2_1)
number2_2 = float(number2)
type5 = type(number2_2)
number23 = 1.75
type6 = type(number23)
number2_3 = int(number23)
type7 = type(number2_3)
boolen1 = bool(1)
boolen2 = bool(0)
type8 = type(boolen1)
print(f"\nstr den int e dönüştürme int(number) {number} {type1} -----> {number1} {type2} \nint den str ye dönüştürme"
      f" str(number2) {number2} {type3} -----> {number2_1} {type4} \nfloat dan int e dönüştürme" 
      f" int(number23) {number23} {type6}-----> {number2_3} {type7}")
print(f"int den float a dönüştürme float(number2) {number2} {type3} -----> {number2_2} {type5} \nint den bool a dönüştürme"
      f"boolen1 = bool(1) -----> {boolen1} {type8} \nint den bool a dönüştürme boolen1 = bool(0) -----> {boolen2} {type8}")

    # 4. Tip dönüşümlerini içerecek şekilde bir program yazınız.
    
number1 = input("Birinci sayıyı giriniz:  ")
number2 = input("İkinci sayıyı giriniz: ")

print("str toplama: ",number1+number2)
print("int toplama: ",int(number1)+int(number2))
print("float toplama: ", float(number1)+float(number2))
    # 5. Kullanıcıdan kendisini tanıtmasını istediğiniz ve aldığınız verileri çeşitli dönüşüm işlemlerine tabi tutarak kullanıcıya çeşitli çıktılar oluşturduğunuz bir program yazınız.
    
    # 6. Operatör kavramını açıklayınız.
""" Python da matematiksel işlemlerini, karşılaştırmaları ve seçenekleri belirlemek için kullanılan sembollerdir.
"""    
    # 7. Pythonda bulunan Operatör türlerini, kullanılan operatörleri belirterek yazınız.
    
"""
Aritmetik Operatörleri :
 = değer atama, + toplama, - çıkarma, * çarpma,
 a+=b     a=a+b,  a-=b  a=a-b, a*=b  a=a*b, a/=b a=a/b, a//=b a=a//b  a%=b  a=a%b 
** üst alma, / Bölme, // Tam bölme, % Bölümde kalma

Karşılaştırma Operatörleri :
== değerler eşit, != değerler eşit değil, 
< küçük, > büyük, <= küçük eşit, >= büyük eşit

Mantıksal Operatörleri :
and iki koşulun da true olması gerekir.
or iki koşuldan birinin true olması yeterlidir.
not koşulun tersini döndürür koşul true ise false false ise true döndürür.
"""
    # 8 
"""
>>> 2**5 
32
>>> 5//2
2
>>> 4+3
7
>>> 11%3
2
>>> 5/2
2.5
>>> 2*5
10
>>> 3-5
-2
>>> (4-1)**2
9
>>> (7//3)/2
1.0
>>> 2**5
32
>>> 5//2
2
>>> 4+3
7
>>> 11%3
2
>>> 5/2
2.5
>>> 2*5
10
>>> 3-5
-2
>>> (4-1)**2
9
>>> (7//3)/2
1.0
>>> 
"""

    # 9
"""
a = 3
a += 2 
print(a)
5

a = 6
a *=3
print(a)
18

a = 5
a **= 3
print(a)
125

a = 11
a %= 3
print(a)
2
"""

    # 10
"""
a = 3
b = 4
print(a == b)
False

a = 6
b = 6
print(a == b)
True

a = 2
b = 1
print(a != b)
True

a = 6
b = 11 
print(a < b)
True

a = 9
b = 7
print(a > b)
True

a = 5
b = 5
print(a >= b)
True
"""
    # 11
"""
a = 5
b = 3
print( a > b and b > 2)
True

a = 6
b = 6
print(a == b and a < 10)
True

a = 2
b = 4
print(a == b or a > b)
False

a = 2
b = 4
print(a != b or a > 8)
True

a = 9
b = 7
print(not(a > b))
False

a = 5
b = 5
print(not(a >= b and a < 1))
True
"""
    # 12 id()  fonksiyonu
"""
id() fonksiyonu, bir nesnenin bellekteki benzersiz kimlik numarasını döndürür.
a = 10
print(id(a))
11760968

"""  
    # 12.
"""
>>> a=10
>>> b=11
>>> c=12
>>> print (a is c)
False
>>> print (a is not b)
True
>>> a+=1
>>> print (a is b)
True
>>> a+=1
>>> print(a is c)
True
>>> 
    
"""