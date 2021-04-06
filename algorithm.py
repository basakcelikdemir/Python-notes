#Algoritma nedir? - Problem cozme teknigidir


# =============================================================================
# Soru1: 0 sayisi girene kadar sayi girisini saglayan ve bu sayilarin 
# ortalamasini hesaplayan programi yazin
# =============================================================================


toplam=0
n=0

while True:
    sayi=input("Bir sayi giriniz(cikis icin 0'a basin):")
    if sayi != "0" :
        if sayi.isnumeric():
            sayi=int(sayi)
            toplam += sayi
            n += 1
        else:
            print("Hatali deger girdiniz.Yeniden tamsayi degeri girini.")
    else:
        print("cikis yapildi.")
        break

if toplam ==0:
    print("hicbir islem yapilmadi")
else:
     print(f"Girilen sayilarin ortalama degeri:{toplam/n}")

# =============================================================================
# # Soru 2: Klavyeden üç kenarı girilen bir üçgenin üçgen olma şartını sağladıktan sonra söz konusu üçgenin eşkenar, ikizkenar ve çeşitkenar üçgen olma durumunu ekrana yazdıran programı yazın.
# 
# # a'nın uzunluğunu giriniz: >? 10
# # b'nin uzunluğunu giriniz: >? 12
# # c'nin uzunluğunu giriniz: >? 23
# # Girilen değerler ile üçgen oluşturamazsın.
# 
# # a'nın uzunluğunu giriniz: >? 6
# # b'nin uzunluğunu giriniz: >? 8
# # c'nin uzunluğunu giriniz: >? 10
# # Çeşitkenar Üçgen
# 
# # a'nın uzunluğunu giriniz: >? 10
# # b'nin uzunluğunu giriniz: >? 10
# # c'nin uzunluğunu giriniz: >? 10
# # Eşkenar Üçgen
# 
# # a'nın uzunluğunu giriniz: >? 12
# # b'nin uzunluğunu giriniz: >? 12
# # c'nin uzunluğunu giriniz: >? 15
# # İkizkenar Üçgen
# 
# =============================================================================

mesaj = """Senden a, b, c adında üç değer istiyoruz.
Bu değerler ile üçgen çeşidini sana yazdırmış olacağız.
"""
print(mesaj)

a = input("a'nın uzunluğunu giriniz: ")
b = input("b'nin uzunluğunu giriniz: ")
c = input("c'nin uzunluğunu giriniz: ")

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a,b,c = int(a) , int(b), int(c)
    a_kenar_sarti = abs(b-c) < a < b+c
    b_kenar_sarti = abs(a-c) < b < a+c
    c_kenar_sarti = abs(a-b) < c < a+b
    if a_kenar_sarti and b_kenar_sarti and c_kenar_sarti:
        if a==b and a==c and c==b:
            print("İkiz kenar ucgen")
        elif a==b or b==c or a==c:
            print("İkiz kenar ucgen")
        else:
            print("cesit kenar ucgen")
    else:
        print("Girilen degerler ile ucgen olusturamazsiniz")
    
    
else:
    print("Kenar degeri tam sayi olmali!")


#THONNY EDITORE BAK

# =============================================================================
# # Soru 3: Girilen n sayısının kendisinden hariç en büyük pozitif tam bölenini bulan programı yazın.
# # Bir n değerini giriniz: 24
# # 24 sayısının kendisi hariç en büyük böleni: 12
# =============================================================================


n = input("Bir n değerini giriniz: ")
if n.isnumeric():
    n=int(n)
    en_buyuk_bolen=0
    for bolen in range(2,n):
        if n % bolen == 0 :
            if bolen > en_buyuk_bolen:
                en_buyuk_bolen=bolen
    print(f"{n} sayisinin kendisi haric en buyuk boleni: {en_buyuk_bolen}")
            
   
else:
    print("Tam sayi giriniz!")


# =============================================================================
# # Soru 4: 100-999 arasındaki basamak değerlerinin küplerinin toplamının kendisine 
#eşit olan sayıların çift olanlarını bir listeye basın ve aritmetik ortalamasını alın.
# # 325.25
# 
# # 1 2 2 != 1 + 8 + 8
# # 1 5 3 == 1 + 125 + 27
# 
# # 1 5 3 % 10 -> 3 153 // 10
# # 1 5 % 10 -> 5
# # 1 % 10 -> 1
# =============================================================================



liste = []
for i in range (100,1000):
    toplam=0
    sayi=i
    while sayi != 0:
        toplam += (sayi % 10)**3
        sayi //=10
    if toplam == i:
        liste.append(i)
        
toplam_dis=0
for num in liste:
    toplam_dis += num
ortalama=toplam_dis/len(liste) 
print(ortalama)       
        
 

# =============================================================================
# # Soru 5: Bir k sayısı tek ise 3 ile çarpılıp 1 ekleniyor, çift ise 2 ile bölünüyor. İşlem, k sayısı 1 olana kadar devam ediyor.
# Bu işlemin kaç adım sürdüğü, işlem sırasında k sayısının aldığı en yüksek değeri k sayısının hangi sayıdan 
#sonra hep çift olarak 1’e ulaştığını bulan programı yazın.
#
# # Beklenen Çıktı
# # Bir k sayısı giriniz: 10
# # 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
# # Uzunluk: 7
# # Serinin en büyük değeri: 16
# # Seri, hangi sayıdan sonra 1'e kadar hep çift gitmiş: 16
# =============================================================================



sayac = 0
en_buyuk = 0
en_buyuk_cift_sayi = 0
k = int(input(("Bir k sayısı giriniz: ")))
while k != 1 and k != 0:
    print(k, end=" --> ")

    if k > en_buyuk:
        en_buyuk = k

    if k % 2 == 0:
        if k > en_buyuk_cift_sayi:
            en_buyuk_cift_sayi = k
        k //= 2
    else:
        k = 3 * k + 1
        en_buyuk_cift_sayi = 0
    sayac += 1
if k != 0:
    print(1)
    print(f"Uzunluk: {sayac+1}")
    print("Serinin en büyük değeri:", en_buyuk)
    print("Seri, hangi sayıdan sonra 1'e kadar hep çift gitmiş:", en_buyuk_cift_sayi)
else:
    print("0 değeri hata verir")








