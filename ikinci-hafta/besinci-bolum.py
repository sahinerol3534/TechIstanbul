

    # 1. Bir menü programı oluşturunuz. (kategori ve yemek alt kategorileri tanımlayarak)
"""
corbalar = ["tavuk suyu", "mercimek","işkembe", "kelle paça", "yayla", "ezo gelin"]
kebablar = ["tavuk şiş", "tire köfte", "kuzu tandır", "karışık ızgara"]
zeytinyaglilar = ["zeytin yağlı enginar", "zeytin yağlı taze fasulye", "karışık kızartma"]
suluyemekler = ["etli kuru fasulye", "salçalı köfte", "tavuk haşlama", "karnıyarık"]
salatalar = ["sezar salatası", "çoban salata", "mevsim salatası", "domates söğüş"]
tatlilar = ["kazandibi", "sütlaç", "künefe", "kemalpaşa", "revani"]
icecekler = ["su", "kola", "meyveli gazoz", "maden suyu", "ayran"]
anayemek = [kebablar, zeytinyaglilar, suluyemekler]
menu = [corbalar, anayemek, salatalar, tatlilar, icecekler]

a = 0
while a < len(menu):
    b = 0
    while b < len(menu[a]):
        if type(menu[a][b]) == list:
            c = 0
            while c < len(menu[a][b]):
                print(menu[a][b][c])
                c += 1
        else:
                print(menu[a][b])
              
        b += 1
    a +=1
"""
    # 2. Yukarıdaki örneği fiyatlı yemeklerin fiyatları olacak şekilde güncelleyiniz. 
        # (Menü oluşturmak için siz manuel giriş yapınız)
"""
corbalar = ["tavuk suyu", "mercimek","işkembe", "kelle paça", "yayla", "ezo gelin"]
fcorbalar  = [150, 100, 125, 200, 225, 130, 110]
kebaplar = ["tavuk şiş", "tire köfte", "kuzu tandır", "karışık ızgara"]
fkebap   = [350, 400, 450, 375]
zeytinyaglilar = ["zeytin yağlı enginar", "zeytin yağlı taze fasulye", "karışık kızartma"]
fzeytinyaglilar = [250, 225, 275]
suluyemekler = ["etli kuru fasulye", "salçalı köfte", "tavuk haşlama", "karnıyarık"]
fsuluyemekler = [300, 310, 325, 335]
salatalar = ["sezar salatası", "çoban salata", "mevsim salatası", "domates söğüş"]
fsalatalar = [75,85, 95, 145, 105, 65]
tatlilar = ["kazandibi", "sütlaç", "künefe", "kemalpaşa", "revani"]
ftatlilar = [115, 135, 140, 155, 165]
icecekler = ["su", "kola", "meyveli gazoz", "maden suyu", "ayran"]
ficecekler = [10, 25, 20, 8, 15]
anayemek = [kebaplar, zeytinyaglilar, suluyemekler]
fanayemek = [fkebap, fzeytinyaglilar,fsuluyemekler]
menu = [corbalar, anayemek, salatalar, tatlilar, icecekler]
fmenu = [fcorbalar, fanayemek, fsalatalar, ftatlilar, ficecekler]
a = 0
while a < len(menu):
    b = 0
    print()
    while b < len(menu[a]):
        if type(menu[a][b]) == list:
            c = 0
            print()
            while c < len(menu[a][b]):
                print(f"{menu[a][b][c]:25}", end = " ---> ")
                print(f"{fmenu[a][b][c]:>4}")
                c += 1
        else:
                print(f"{menu[a][b]:25}", end = " ---> ")
                print(f"{fmenu[a][b]:>4}")

              
        b += 1
    a +=1
"""

    # 3. Yukarıdaki örneği bir sipariş haline getirip, kullanıcının seçtiği yemekler için 
        # ödeyecek olduğu hesabı belirten hale getiriniz. (Hazır bir menü sistemi oluşturup hesaplamaları yapınız. 
        # Önceki çıktıları kullanabilirsiniz)

"""
print("*" * 5, "Yemek Listesi", "*" * 5)
print(" *  çorbalar:")
print(" 11. tavuk suyu\n 12. mercimek\n 13. işkembe\n 14. kelle paça\n 15. yayla\n 16. ezo gelin")
print(" * Anayemek / kabaplar:")
print(" 21. tavuk şiş\n 22. tire köfte\n 23. kuzu tandır\n 24. karışık ızgara")
print(" * anayemek / zeytinyağlilar:")
print(" 31. zeytin yağlı enginar\n 32. zeytin yağlı taze fasulye\n 33. karışık kızartma")
print(" * anayemek / suluyemekler:")
print(" 41. etli kuru fasulye\n 42. salçalı köfte\n 43. tavuk haşlama\n 44. karnıyarık")
print(" * salatalar:")
print(" 51. etli kuru fasulye\n 52. çoban salata\n 53. mevsim salatası\n 54. domates söğüş")
print(" * salatalar")
print(" 51. etli kuru fasulye\n 52. çoban salata\n 53. mevsim salatası\n 54. domates söğüş")
print (" * içecekler:")
print(" 61. su\n 62. kola\n 63. meyveli gazoz\n 64. maden suyu\n 65. ayran")
print(" 0. çıkış")


corbalar = ["tavuk suyu", "mercimek","işkembe", "kelle paça", "yayla", "ezo gelin"]
fcorbalar  = [150, 100, 125, 200, 225, 130, 110]
kebaplar = ["tavuk şiş", "tire köfte", "kuzu tandır", "karışık ızgara"]
fkebap   = [350, 400, 450, 375]
zeytinyaglilar = ["zeytin yağlı enginar", "zeytin yağlı taze fasulye", "karışık kızartma"]
fzeytinyaglilar = [250, 225, 275]
suluyemekler = ["etli kuru fasulye", "salçalı köfte", "tavuk haşlama", "karnıyarık"]
fsuluyemekler = [300, 310, 325, 335]
salatalar = ["sezar salatası", "çoban salata", "mevsim salatası", "domates söğüş"]
fsalatalar = [75,85, 95, 145, 105, 65]
tatlilar = ["kazandibi", "sütlaç", "künefe", "kemalpaşa", "revani"]
ftatlilar = [115, 135, 140, 155, 165]
icecekler = ["su", "kola", "meyveli gazoz", "maden suyu", "ayran"]
ficecekler = [10, 25, 20, 8, 15]
anayemek = [kebaplar, zeytinyaglilar, suluyemekler]
fanayemek = [fkebap, fzeytinyaglilar,fsuluyemekler]
menu = [corbalar, anayemek, salatalar, tatlilar, icecekler]
fmenu = [fcorbalar, fanayemek, fsalatalar, ftatlilar, ficecekler]
a = 0
secilenMenu = []
secilenmenufiyat = []
while True:
    yemekNo = input("Yemeklerinizi sıra no girerek seçiniz.: ")
    if yemekNo.strip() == "":
        break
    yemekNo = int(yemekNo)
    if yemekNo == 0:
        break 
    yemekNo = int(yemekNo)
    if yemekNo >= 11 and yemekNo <= 16:
        match yemekNo:
            case 11:
                secilencorba = corbalar[0]
                secilencorbafiyati = fcorbalar[0]
            case 12:
                secilencorba = corbalar[1]
                secilencorbafiyati = fcorbalar[1]
            case 13:
                secilencorba = corbalar[2]
                secilencorbafiyati = fcorbalar[2]
            case 14:
                secilencorba = corbalar[3]
                secilencorbafiyati = fcorbalar[3]
            case 15:
                secilencorba = corbalar[4]
                secilencorbafiyati = fcorbalar[4]
            case 16:
                secilencorba = corbalar[5]
                secilencorbafiyati = fcorbalar[5]

        
        secilenMenu.append(secilencorba)
        secilenmenufiyat.append(secilencorbafiyati)
    if yemekNo >= 21 and yemekNo <= 24:
        match yemekNo:
            case 21:
                secilenkebap = kebaplar[0]
                secilenkebapfiyati = fkebap[0]
            case 22:
                secilenkebap = kebaplar[1]
                secilenkebapfiyati = fkebap[1]
            case 23:
                secilenkebap = kebaplar[2]
                secilenkebapfiyati = fkebap[2]
            case 24:
                secilenkebap = kebaplar[3]
                secilenkebapfiyati = fkebap[3]
        secilenMenu.append(secilenkebap)
        secilenmenufiyat.append(secilenkebapfiyati)

    if yemekNo >= 31 and yemekNo <= 33:
        match yemekNo:
            case 31:
                secilenzeytinyaglilar = zeytinyaglilar[0]
                secilenzeytinyaglilarfiyati = fzeytinyaglilar[0]
            case 32:
                secilenzeytinyaglilar = zeytinyaglilar[1]
                secilenzeytinyaglilarfiyati = fzeytinyaglilar[1]
            case 33:
                secilenzeytinyaglilar = zeytinyaglilar[2]
                secilenzeytinyaglilarfiyati = fzeytinyaglilar[2]
           
        secilenMenu.append(secilenzeytinyaglilar)
        secilenmenufiyat.append(secilenzeytinyaglilarfiyati)

    if yemekNo >= 41 and yemekNo <= 44:
        match yemekNo:
            case 41:
                secilensuluyemekler = suluyemekler[0]
                secilensuluyemeklerfiyati = fsuluyemekler[0]
            case 42:
                secilensuluyemekler = suluyemekler[1]
                secilensuluyemeklerfiyati = fsuluyemekler[1]
            case 43:
                secilensuluyemekler = suluyemekler[2]
                secilensuluyemeklerfiyati = fsuluyemekler[2]
            case 44:
                secilensuluyemekler = suluyemekler[3]
                secilensuluyemeklerfiyati = fsuluyemekler[3]
           
        secilenMenu.append(secilensuluyemekler)
        secilenmenufiyat.append(secilensuluyemeklerfiyati)

    if yemekNo >= 51 and yemekNo <= 54:
        match yemekNo:
            case 51:
                secilensalatalar = salatalar[0]
                secilensalatalarfiyati = fsalatalar[0]
            case 52:
                secilensalatalar = salatalar[1]
                secilensalatalarfiyati = fsalatalar[1]
            case 53:
                secilensalatalar = salatalar[2]
                secilensalatalarfiyati = fsalatalar[2]
            case 54:
                secilensalatalar = salatalar[3]
                secilensalatalarfiyati = fsalatalar[3]
           
        secilenMenu.append(secilensalatalar)
        secilenmenufiyat.append(secilensalatalarfiyati)

    if yemekNo >= 61 and yemekNo <= 65:
        match yemekNo:
            case 61:
                secilenicecekler = icecekler[0]
                secileniceceklerfiyati = ficecekler[0]
            case 62:
                secilenicecekler = icecekler[1]
                secileniceceklerfiyati = ficecekler[1]
            case 63:
                secilenicecekler = icecekler[2]
                secileniceceklerfiyati = ficecekler[2]
            case 64:
                secilenicecekler = icecekler[3]
                secileniceceklerfiyati = ficecekler[3]
            case 65:
                secilenicecekler = icecekler[4]
                secileniceceklerfiyati = ficecekler[4]
           
        secilenMenu.append(secilenicecekler)
        secilenmenufiyat.append(secileniceceklerfiyati)
           

#print(secilenMenu)
#print( secilenmenufiyat)
print("\n*** Seçtiğiniz Menu ***")
total = 0
for i in range(len(secilenMenu)):
   print(f"{secilenMenu[i]:20} -----> {secilenmenufiyat[i]:>4} TL")
   total += secilenmenufiyat[i]

print(f"{'menu toplam fiyat :':20} -----> {total:>4} TL")
"""

    # 4. Bir öğrenci tanıma kartı oluşturunuz. öğrenciye adi, soyadı gibi bilgileri sorduktan sonra, 
        # derslerini ve derslerine ait notları sorup toplu çıktı veren bir sistem yazınız. (bir nevi cv gibi)
"""
firstName = input("Adınızı giriniz.:  ") 
lastName = input("Soyadınızı giriniz.: ")
print(f"Hoşgeldin {firstName.capitalize()} {lastName.upper()}.")
print(f" {firstName.capitalize()} derslerini ve bu derslerden aldığın notları giriniz.: ")
i = 0
lessons = []
points = []
while True:
    lesson = input("Dersin adını giriniz: ")
    if lesson == "":
        break
    point = float(input("Dersin Notunu giriniz.: "))
    lessons.append(lesson)
    points.append(point)
    i += 1
    
# print(lessons)
# print(points)
print(f"\nAdı Soyadı: {firstName.capitalize()} {lastName.upper():30}")
print(f"{'Dersin Adı':20}{'Geçme Notu'}")
for i in range(len(lessons)):
    print(f"{lessons[i].capitalize():20}{points[i]:>4}")
"""
    
    # 5. bir todo list oluşturunuz. oluşturacak olduğunuz yapılacaklar listesinde kullanıcıya görevleri sorunuz, 
        # görev listesini yapınız, görevlerin durumunu kontrol ediniz ve tüm görevler tamamlanınca teşekkür ederek 
        # programı tamamlayınız.
"""
print("\n***** Yapılacak İşler *****")
todos = ["kapıyı sil", "pencereleri sil", "merdiveni paspasla", "çöpü at", "markete git", "bankaya para yatır"]
i = 1
for todo in todos:
    print(f"{i}. {todo.capitalize()}")
    i += 1
firstName = input("adınızı giriniz.: ")
orders = []
print("\n*****",firstName," için Gorev Listesi *****")
for j in range(len(todos)):
    order = input("Görevinizin sıra nosunu giriniz.: ")
    if order == "":
        break
    orders.append(order)
number = 0
for order in orders:
    boolen = input("Görevinizi tamamladınız mı? (e/h).: ")
    if boolen.lower() == "e":
        number += 1
orderisok = int(number / len(orders) * 100)
print()
if orderisok <= 20:
    print(f"Görevinizi %{orderisok} tamaladınız.")
    print("görevinizi yapmalısınız..!")
elif 20 < orderisok <= 40:
    print(f"Görevinizi %{orderisok} tamaladınız.")
    print("görevinizi tamamlamak için gayret gösteriniz..!")
elif 40 < orderisok <= 60:
    print(f"Görevinizi %{orderisok} tamaladınız.")
    print("Çalışmanız vasat biraz daha çalışmalısınız..!")
    
elif 60 < orderisok <= 80:
    print(f"Görevinizi %{orderisok} tamaladınız.")
    print("görevinizi tamamlamaya az kaldı..!")
   
else:
    print(f"Görevinizi %{orderisok} tamaladınız.")
    print("Tebrikler görevinizi tamamladınız.")
"""

    # 6. yukarıdaki örnek için görev kategorileri tanımlayarak örneği tekrar yapınız.
"""
print("\n***** Yapılacak İşler *****")
outdoortodos = ["çöpü at", "markete git", "bankaya para yatır"]
indoortodos = ["kapıyı sil", "pencereleri sil", "merdiveni paspasla", "çöpü at"]
todos = [outdoortodos + indoortodos]

a = 0
i = 0
while a < len(todos):
    b = 0
    i += 1
    while b < len(todos[a]):
        print(f"{i}. {todos[a][b]:25}")
        i += 1
        b += 1
    a +=1
"""
    # 7. yukarıda ki örneği görev kategori ve alt görevler şeklinde güncelleyerek tekrar yapınız.


    # 8. böl ve feth et algoritmasını araştırarak, fonksiyon kullanmadan listeler aracılığı ile kullanıcıdan 
        # alacak olduğunuz sayılar arasındaki en büyük ve en küçük sayıları hesaplatarak ekrana yazdırınız. 
        # (bu biraz uğraştırıcı)
"""
i = 0
numbers = []
while True:
    number = input("Bir Sayı giriniz.(bitirmek için enter) : ")
    if number == "":
        break
    number = int(number)
    if number == 0:
        break
    numbers.append(number)
    i += 1
print(numbers)

maxNumber = numbers[0]
minNumber = numbers[0]
j = 1
while j < len(numbers):
    if numbers[j] > maxNumber:
        maxNumber = number[j]
    if numbers[j] < minNumber:
        minNumber = numbers[j]
    j += 1
print("girilen sayılar:")
for number in numbers:
    print(number, end = ", ")
print("En küçük sayı: ", minNumber)
print("En büyük sayı: ", maxNumber)
"""
"""
if len(numbers) > 0:
    stack = [(0, len(numbers) - 1)]
    maxNumber = numbers[0]
    minNumber = numbers[0]

    while stack:
        left, right = stack.pop()
        if left == right :
            if numbers[left] > maxNumber:
                maxNumber = numbers[left]
            if numbers[left] < minNumber:
                minNumber = numbers[left]

        elif right - left == 1:
            if numbers[left] < numbers[right]:
                if numbers[left] < minNumber:
                    minNumber = numbers[left]
                if numbers[right] > maxNumber:
                    maxNumber = numbers[right]
            else:
                if numbers[right] < minNumber:
                    minNumber = numbers[right]
                if numbers[left] > maxNumber:
                    maxNumber = numbers[left]
        else:
            mid = (left + right) // 2
            stack.append((left, mid))
            stack.append((mid + 1, right))
    print("en küçük sayı: ", minNumber)
    print("en büyük sayı: ", maxNumber)
else:
    print("Sayı girilmedi..!")
"""

    # 9. kullanıcıdan n tane sayı girmesini isteyerek, hangi sayıyı kaçar tane girdiğini 
        # kullanıcıya söyleyen programı yazınız.
"""
amount = int(input("Kaç adet sayı girmek istersiniz?  "))
if amount > 0 :
    numbers = []
    counts = []
    for i in range(amount):
        number = input(f"{i+1}. sayıyı giriniz.: ")
        numbers.append(number)
    print(numbers)
    for j in range(len(numbers)):
        count_ = numbers[j]
        if count_ not in counts:
            counts.append(count_)
            print(count_,"sayısı",numbers.count(count_),"kez girildi.")

else : 
    print("sıfırdan büyük bir sayı girmeniz gerekiyor..!")
"""


    # 10. kullanıcıya en sevdiği yazarları ve bu yazarlara ait en sevdiği eserleri sorarak, 
        # aldığı verileri gruplar halinde listeyen uygulamayı yazınız.

"""
i = 0
yazarlar = []
kitaplar = []
turler = []
kitaplistesi = []
while True:
    yazar = input("sevdiğiniz yazar adını giriniz. :")
    if yazar == "":
        break
    kitap = input ("sevdiğniz yazara ait kitabı giriniz.: ")
    kitapturu = input("kitap türünü giriniz.: ")
    liste = [kitap,yazar, kitapturu]
    kitaplistesi.append(liste)
print(kitaplistesi)
print(f"{'kitap adı':20} {'yazarı':20} {'türü'}")
for i in range(len(kitaplistesi)):
    print(f"{kitaplistesi[i][0]:20} {kitaplistesi[i][1]:20} {kitaplistesi[i][2]}")
"""

    # 11. 2 den 1000'e kadar olan asal sayıları bulan ve yazdıran programı yazınız.
"""
asal = []
for i  in range(2, 1000):
    asalmi = True
    for j in range(2, int((i**0.5)+1)):
        if i %j == 0:
            asalmi = False
            break
    if asalmi:
        asal.append(i)
print(asal)
"""

