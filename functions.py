#Fonksiyon nasıl yazilir?

def kare_al(x):
    print(x**2)
kare_al(2)

#BILGI NOTUYLA CIKTI URETMEK

def kare_al(x):
    print("Girilen Sayi: "+ str(x) )
    print("Girilen Sayinin Karesi: " + str(x**2))
kare_al(2)

#IKI ARGUMANLI FONKSIYON TANIMLAMAK

def carpma_yap(x,y):
    print(x*y)
carpma_yap(3,6)    

# ON TANIMLI ARGUMANLAR

def carpma_yap(x,y=1):
    print(x*y)
carpma_yap(3)  #y degeri girmedik fakat on tanimlide 1 oldugu icin 1 ile carpti

#Fonksiyon ciktilerini girdi olarak kullanmak:return

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

cikti=direk_hesap(25,40,70) 
cikti #cikti olarak geldi,sonucu gelmedi!!!!


def direk_hesap(isi,nem,sarj):
    return(isi+nem)/sarj

direk_hesap(25,40,70) *9 #○cikti girdi olarak aldik
cikti=direk_hesap(25,40,70)
cikti 

#Local Etki Alanindan Global Etki Alanini Degistirme

x=[]      #Global etki alani
def eleman_ekle(y):
    x.append(y)   #y degerini x listesine ekle
    print(str(y)+ "ifadesi eklendi")  #local etki alani
    
#Sorgular(Karar-Kontrol)
#*TRUE/FALSE
sinir=5000
sinir==6000 #sinir 5000 mi? (false)

#*IF-ELIF-ELSE

sinir=4000
gelir=4000

if gelir < sinir: #eger gelir sinirdan kucukse
    print("Gelir sinirdan kucuk") #gelir sinirdan kucuktur yaz
elif gelir > sinir: #eger gelir sinirdan buyukse
    print("Gelir sinirdan buyuk") #gelir sinirdan buyuktur yaz
else:
    print("Gelir sinira esittir")    #diger durumlar da esittir yaz
    
    
# =============================================================================
# MINI UYGULAMA
# ornek: gelir sinirdan buyukse tebrik et,kucukse uyarı yaz
# =============================================================================


sinir=50000
magaza_adi=input("Lutfen Magaza Adini Giriniz! :")
gelir=int(input("Lutfen Gelirinizi Giriniz! : ")) #inputtan gelen deger str
                                                 #gelir int cevirmemiz gerekir
                                                     
if gelir > sinir:
    print("Tebrikler "+ magaza_adi + "promosyon kazandiniz")
elif gelir < sinir:
    print("Uyari! Cok dusuk gelir: " + str(gelir))
else:
    print("Basarilar")    


#DONGULER - FOR

# =============================================================================
# ornegin bir liste icersindeki her bir elemana
# tek tek gidip o elemanlara islem uygulamak istedigimizde
# o elemanlara tek tek gitmeyi saglar
# =============================================================================

ogrenci=["ali","veli","isik","berk"]

for i in ogrenci: 
    print(i)


# =============================================================================
#  For- Mini Ornek
# maasi 3000 den kucuklere %25 zam yap
# maasi 3000 den buyuk ve esit  6000 den kucuklere %15 zam yap
# maasi 6000 den buyuk esit olanlara da %5 zam yap
# ciktiya maasi,zam miktari,zamli maasini yazdir
# 
# =============================================================================


maaslar=[1000,2000,3000,4000,5000,6000,7000]
for i in maaslar:
    if i < 3000:
        print("maasiniz: "+ str(i))
        print("zam miktariniz: " + str((i*25)/100) )
        print("zamli maasiniz : " + str((i*25)/100+i))
    elif i < 6000:
        print("maasiniz: "+ str(i))
        print("zam miktariniz: " + str((i*15)/100) )
        print("zamli maasiniz : " + str((i*15)/100+i))
    else:
        print("maasiniz: "+ str(i))
        print("zam miktariniz: " + str((i*5)/100) )
        print("zamli maasiniz : " + str((i*5)/100+i))

#BREAK & CONTINUE

# =============================================================================
# donguler Icerisinde bazen belirli sarti saglayan
# ifadeler yakalandiginda (ifler ile) 
# dongu bitirilmek istenebilir (break) 
# ya da  gormezden gelinmek istenebilir(continue)
# =============================================================================

maaslar2=[8000,5000,2000,1000,3000,7000,1000] #sirasiz
maaslar2.sort()

for i in maaslar2:            #i degeri
    if i == 3000:             #3000 esit olunca
        print("kesildi")      #donguyu bitirir ve kesildi yazdir
        break
    print(i)


for i in maaslar2:           
    if i == 3000:           #i degeri
       continue             #3000 esit olunca
    print(i)                #o degeri gorme gec
   

#WHILE

# =============================================================================
# Oldugu surece,bu sart saglandigi surece
# =============================================================================

sayi = 1

while sayi < 10: #sayi 10 dan kucuk oldugunca
    sayi += 1  #sayiya 1 ekleyip arttir
    print(sayi)


# NESNE YONELIMLI PROGRAMLAMA(OOP)

# =============================================================================
# siniflar nedir?:benzer ozellikler ortak amaclar 
#             tasiyan gruplar olusturmak i̇ci̇n
# =============================================================================


#ORNEK OZELLIKLERI

class VeriBilimci():
    bildigi_diller=["R","PYTHON"]
    bolum=''
    sql= ''
    deneyim_yili=0
    def __init__(self):
        self.bildigi_diller=[]   
        self.bolum=""  
        self.deneyim_yili=[]
        
  #her bir ornegin kendi icinde degisen
  # ozelliklerden olustugu bilgisini ermek
  #(ornek ozelligi tanimlamaktir bu)       
        
        
                              
ali=VeriBilimci()
ali.bildigi_diller.append("PYTHON")
ali.bolum="istatistik"
ali.deneyim_yili.append("7 yil")

veli=VeriBilimci()
veli.bildigi_diller.append("R")
veli.bolum="end_muh"
veli.deneyim_yili.append("8 yil")

VeriBilimci.bildigi_diller
VeriBilimci.bolum


#ORNEK METODLARI

# =============================================================================
# mesela her bir veribilimci  
# yeniogrenilen dilin veri bilimcinin
# bildigi dillere ekleme yapsin 
# =============================================================================

class VeriBilimci():
    calisanlar=[]
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=''
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)

ali=VeriBilimci()        
veli=VeriBilimci()      
 
VeriBilimci.dil_ekle(ali,"R")  # ya da
ali.dil_ekle("R") 
ali.bildigi_diller

#MIRAS YAPILARI

class Employees():
    def __init__(self):
        self.FirstName=''
        self.LastName=''
        self.Address='' 
        
class DataScience(Employees):  ##employees'in ozellikleri digerlerine ekledik
    def __init__(self):
        self.Programming=''
     
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling=''


#Python'da Fonksiyonel Pogramlama

# =============================================================================
# Fonksiyonlar dilin bas tacidir
# (Birinci sinif nesnelerdir)
# Yan etkisiz fonksiyonlar(stateless,girdi-cikti)
# Yüksek seviye fonksiyonlar
# Vektorel operasyonlar
# =============================================================================

# Yan etkisiz fonksiyonlar(Pure Functions)

#Ornek:Yan etki

A=9

def impure_sum(b):
    return b+A
def pure_sum(a,b):
    return a+b

impure_sum(6)  #a degistikce sonuc degisiyor
               #safolmayan
               #yanetki  demek
               #bagimli demek
               
pure_sum(3,4)     #ancak girdi verdiginde ciikti uretir
                  #disaridan etkilemez
                  

#Ornek: Olumcul Yan etkiler
##OOP
class LineCounter:
    def __init__(self,filename):
        self.file=open(filename,'r')
        self.lines=[]
     
    def read(self):
        self.lines=[line for line in self.file]     #bir dosya okuma islemi
     
    def count(self):
        return len(self.lines)
    
lc=LineCounter('deneme.txt')

print(lc.lines)  #bos
print(lc.count()) #sifir degeri geldi

lc.read()
print(lc.lines) #satirlarda ne yazdigi
print(lc.count()) #kac satir yazildiginin sayilmasi sonucu
    
#bu degiskenlik durumu rahatsiz edicidir.bazen bir problemdir
#pure olmayan 
  
##FP(fonksiyonel programlama)            
  
def read(filename):
   with open(filename,'r') as f:
       return[line for line in f] #okuma ve sayma fonksiyonlariyla
 
def count (lines):
   return len(lines)

example_lines=read('deneme.txt')
lines_count=count(example_lines)
lines_count

#bir girdi verdigimizde cikti uretecek
#baska hicbir yapiyi etkilemez
#pure

#ISIMSIZ FONKSIYONLAT(ANONYMOUS FUNCTIONS)
#Lambda

def old_sum(a,b):   #olusturdugumuz fonksiyona isim verdik
    return a+b
    old_sum(4,5)


new_sum=lambda a,b : a+b   #isim vermedik
new_sum(4,5)



sirasiz_liste=[("b",3),("a",8),("d",12),("c",1)]

#amac:liste icerisinde ki tupleri siralamak
      #1.indekse gore

sorted(sirasiz_liste,key=lambda x:x[1])

#VEKTOREL OPERASYONLAR(VECTOREL OPERATIONNS)
##OOP
a=[1,2,3,4]
b=[2,3,4,5] 

#her bir elemani birbiriyle carpmak amacimiz

ab=[]
for i in range(0,len(a)):
    ab.append(a[i]*b[i])

##FP

import numpy as np 

#( numpy adli kutuphaney
#calisma dizinime dahil ettim)

a=np.array([1,2,3,4])
b=np.array([1,2,3,4])

a*b

#MAP & FILTER & REDUCE

# =============================================================================
# *MAP*
# verilen bir vektorun icersinde
# belirli bir fonksiyonu(isimsiz) calistirma imkani verir
# =============================================================================


liste=[1,2,3,4,5]

for i in liste:
    print(i+10)
    
list(map(lambda x:x+10,liste))


# =============================================================================
# *FILTER*
#  benzer sekilde bir fonksiyon ve
#  iteratif bir nesne alir bu nesne 
#  Uzerinden baska bir iteratif nesne olusturulur
#  ve iteratif nesne icerisinden aradigi sarti saglandigi
#  tum elemanlar filtrelenir
# =============================================================================


liste=[1,2,3,4,5,6,7,8,9,10]
cift_sayilar=list(filter(lambda x: x % 2 ==0,liste))

# =============================================================================
# *REDUCE*
# indirgemek demektir
# =============================================================================


from functools import reduce 
# functools modulu(kutuphane) icerisinden reduce fonksiyon cagiriyoruz

liste=[1,2,3,4]
reduce(lambda a,b : a + b, liste)
 

#MODUL(kutuphane,paket) OLUSTURMAK

# =============================================================================
# *MODUL*:belirli amaclari yerine getirmek icin
# birarada bulunan fonksiyonlar toplulugudur
# =============================================================================

import HesapModulu  #yeni sayfa actim hesap modulu adli
HesapModulu.yeni_maas(1000)

import HesapModulu as hm
hm.yeni_maas(2000)

from HesapModulu import yeni_maas #modulun fnksiyonu direkt cagirilir

yeni_maas(5000)

import HesapModulu as hm
hm.maaslar         #listeyi cagirdik


#HATALAR / ISTISSNALAR( exceptions)
#1.kullanici hatalari
#2.bug
#3.istisnalar(exceptions)

# =============================================================================
# 3. :::::ISTISNALAR(expections)::::::
# #programda bildigimiz bazi hatalar var 
# bu hatalar gozlemlendiginde calismayi durdurma 
# calismaya devam et 
# =============================================================================

#ZeroDivisionError hatasi

a=10
b=0
a/b     #hata verir

try:
    print(a/b)
except ZeroDivisionError: 
    print("Payda da sifir olmaz")
    
#a/b geldiginde bir dene onceki satirlara bagi var
#eger calismazsa hatali islem olursa
#sen calistirmayi surdur ve mesaj yayinladik

#TypeError:

a=10
b="2"

a / b #hata verir.

try:
    print(a/b)
except TypeError:
    print("sayi ve string problemi")