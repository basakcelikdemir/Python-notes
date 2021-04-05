#STRING METODLAR

## dir(gel_yaz) -> hangi metodlari kullanabilecegimiz listesi
gel_yaz="Gelecegi_yazanlar"
gel_yaz.upper() #harfleri buyutur
gel_yaz.lower() #harfleri kucultur
gel_yaz.capitalize() # cumlenin bas harfi buyutur
gel_yaz.title() #kelimlerin bas harfini buyutur
gel_yaz.islower() #harfler kucuk mu? (sorgu)
gel_yaz.isupper() #harfler buyuk mu? (sorgu)
gel_yaz.startswith("Gelecegi") #gelecegi ile mi baslar(sorgu)
gel_yaz.endswith("yazanlar") # ne ile biter(sorgu)
gel_yaz.isidentifier() #degisken adi olabilir mi(sorgu)
gel_yaz.isprintable() #yazdirilabilir ifademi(kacis karakteri olmaz)
gel_yaz.isspace() #sadece bosluklardan olusursa
len(gel_yaz) #boyutunu verir
gel_yaz.replace("a","i") #cümlede a harflerini i harfine cevir
gel_yaz1="*gelecegi_yazanlar*"
gel_yaz1.strip("*") #yildizlari siler
gel_yaz1.lstrip("*") #soldaki yildizi sil
gel_yaz1.rstrip("*") #sagdaki yildizi sil

"-DSMLBC5-".ljust(50,"#") #bir metinsel ifadeyi belirtilen karakter ile 
                        #belirtilen sayi kadar doldurur ve ifadeyi sola yaslar
"-DSMLBC5-".rjust(50,"#") #saga yaslar
"-DSMLBC5-".center(50,"#") #iki tarafa yaslar

"Ali Ata Bakma Uzaya Git".split() #cümlenin her kelimesini listeye donusturuyor
"Ali Ata Bakma Uzaya Git".rsplit(" ", 2) #sagdan belirtilen sayiya kadar gider
                                         # elemana boler.


" ".join(['Ali', 'Ata', 'Bakma', 'Uzaya', 'Git']) #listeyi metine cevirdi

"masat".translate(str.maketrans("st","rz")) #masatı maraza cevirdi.birden fazla 

                                           #harf degitmek gerekince bunu kullaniriz
pi_sayisi=3.144159265358
pi_mesaj="pi sayisi:"+str(pi_sayisi)
                                       #iki türlü yazabiliriz
pi_mesaj=f"Pi sayisi: {pi_sayisi}"

pi_mesaj=f"Pi sayisi: {pi_sayisi:.4f}" #virgulden sonra 4 basamak al

print("bu ifade \nYeni satırda yazildi") #\n yeni satira gecmeyi saglar
print("bu ifade \tYeni satırda yazildi") #\t tab boslugu koymayi saglar

#KARAKTER DIZILERINDE ALT KUME ISLEMLERI
gel_yaz[0] #0.indeksi verir yani G harfini

#TYPE_DONUSUMLERI

toplama_bir=input("bir sayi giriniz!:\t") #kullanicidan sayi al
toplama_iki=input("bir sayi giriniz!:")

#input alinca otamatikmen str oluyor bunu 
#int cevirmemiz gerekir.

toplam = int(toplama_bir)+int(toplama_iki)

print("gelecegı","yazanlar",sep="_") #iki kelimeyi _ ile birlestir
print("DMSLBC\nPython\nEtüt\nDersleri") # degerleri alt alta cikarir
print("DSMLBC" ,"Python", "Etüt", sep="\n")


print("DSMLBC",end=" ")
print("Python",end=" ")   #4 printi birlestirdi
print("etüt",end=" ")
print("Dersleri")

print(*"python") #liste gibi her bir harfi ayiriyor

#VERI YAPILARI

##listeler ->

# **degistirilebilir
# **kapsayicidir(farkli tipte verileri tutabilir)
# **siralidir(indeks)
 
notlar=[90,80,70,50,50,70,80]
liste=["ali","veli","isik"]
liste=[liste,notlar]
len(liste)
notlar.append(15) #notlar adli listeye 15i ekledi
notlar.remove(15) #15i cikardik
liste.insert(0,"ayse") #indekse gore ekleme yapti
liste[0]="ayse" #ali uctu(hata)
liste.pop(0) #0.indeksi sildi
notlar.count(80) #Notlar adli listede kac tane 80 var?
notlar_yedek=notlar.copy() #notlar adli listeyi yedekledi(kopyaladi)
notlar.extend(["a","b",10]) #farkli tiplerde eklememizi saglar
notlar.index("a") #indeks bilgisini verir
notlar.reverse() #elemanlari ters cevirir
notlar.sort() #kucukten buyuge siraladi
notlar.clear() #notlar adli listenin elemanlarini sildi(temizledi)

##tuple(Demet) ->

# **degistirilemez
# **kapsayicidir(farkli tipte verileri tutabilir)
# **siralidir(indeks)

t=("ali","veli",1,2,3.2,[1,2,3,4]) #() tuple olusturur
t=("eleman",) #tek elemanli yapsaydik str anlardi.virgul koyarak tuple oldugunu belirttik


##Dictionary(Sozluk) ->

# **degistirilebilir
# **kapsayicidir(farkli tipte verileri tutabilir)
# **sirasiz(indekssiz)

sozluk={'REG': 'Regresyon Modeli',
 'LOJ': 'Lojistik Regresyon',
 'CART': 'Classification and Reg'}


sozluk["REG"] #keylerle cagiririz
sozluk["GBM"]="Gradient Boosting" #yeni bir key value ekledik
sozluk["REG"]="Coklu Dogrusal Regresyon" #olan key'in value degerini degistirdik


##Setler(kumeler) ->

# **degistirilebilir(degistirilen frozensetler olur)
# **kapsayicidir(farkli tipte verileri tutabilir)
# **sirasiz(indekssiz)
# **degerleri essiz

s=set([1,"a","b"])

ali="lutfen_ata_bakma_uzaya_git"
s=set(ali) #ali degiskenindeki karakterleri tek bir tane olarak aldi

l=["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]

s=set(l) #tekrarli elemanlari almadi

s.add("ile") #ile'yi ekledi
s.remove("ile") #ile'yi sildi
s.remove("ile") #ile'yi bir daha silersek hata verir.
s.discard("ile") #kumede ile elemanı yok fakat hata uretmez(bu eleman varsa sil yoksa hata uretme)


# =============================================================================
# 
# #Klasik Kume Islemleri
# 
# difference() ile iki kumenin farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symmetric_difference() ikisinde de olmayanlari
# =============================================================================

#kod blogu yapma= Ctrl+4 ya da Alt+4
#tek satır yorum satırı olusturma = Ctrl+1

 # DIFFERENCE()

set1=set([1,3,5])
set2=set([1,2,3])

set1.difference(set2) #set1 de olup set2 de olmayan
set1-set2 #set1 de olup set2 de olmayan

set1.symmetric_difference(set2) #ikisinde olmayan

# INTERSECTION() &  UNION() 

kesisim=set1&set2 #kesisim elemanları
kesisim
birlesim=set1.union(set2) #birlesme
birlesim


set1.intersection_update(set2) ##kesisimin ifadeleri set1in oldu.guncellendi

#Sorgular
set1=set([7,8,9])
set2=set([5,6,7,8,9,10])



set1.isdisjoint(set2) # iki kumenin kesisiminin bos olup olmadiginin sorgulamasi
set1.issubset(set2) #set1 set2nin alt kumesi midir?
set2.issuperset(set1) #set2 set1i kapsar mı?