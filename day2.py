faiz = 1.59
vade = "36"
krediAdi =  "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


# tip değişimi yaparken değişim şartı olarak değişime uygun olması lazım mesela krediAdi tip dönüşümüne uygun değil
print(int(vade)+12)

faiz = str(faiz)
print(type(faiz))

print(str(faiz))

vade = 36 #int(input ("Lütfen istedğiniz vade sayisini giriniz:"))

print(type(vade))
vade = vade + 12

# string interpolation
# sectiğniz vade sonucu ortaya çıkan vade
print("sectiğniz vade sonucu ortaya çikan vade:" + str(vade))
print("seçtiğiniz vade sonucu ortaya çikan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Doğukan"
metin = "Merhaba {name}".format(name=123)
print(metin)

# f-string
metin = f"Hoşgeldiniz {isim}"
print(metin)


#listeler
#döngüler

krediler =["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))

print(krediler[2])

#bir listede kaç değer var öğrenme fonksiyonu

print(len(krediler)) #lenght in kısaltılmısından gelir

dizi = ["İhtiyaç Kredisi",10,5.2]
print(dizi[2])

#bir objeyi dizinin sonuna eklemek istiyosak eğer
krediler.append("Öğrenci Dostu Kredi")
print(krediler)
 
krediler.append("X Kredisi")
print(krediler)

# istediğimiz indexteki objeyi silmeye yarıyor
krediler.pop(2)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

#bu objeden 2 tane var ilk bu objeyi nerede görürse o objeyi siler
krediler.remove("Taşıt Kredisi")
print(krediler)

#tek satırda obje eklemek için 
krediler.extend(["Y Kredisi","M Kredisi"])
print(krediler)


# for döngüsü
#range i nin başladığı sayıdan 1 arttırarak içindeki sayıya kadar sayar
#bir başlangıç belirtmezsek 0dan başlar
for i in range(10):
    print("Beşiktaş")
    print(i)
print("**************************")

#range 2. değeri kaçta bitecek onu gösterir
for i in range(5,10):
    print(i)
print("******************")

#range 3. değeri kaç kaç artacak onu belirtir
for i in range(0,51,5):
    print(i)    

#range döngüsü bizden int değeri ister float verince hata gösterir

krediler =["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]

for kredi in krediler:
    print(kredi)

print("*********************")

for i in range(len(krediler)):
    print(krediler[i])
print("**************************")

#sonsuz döngü
i=0
while i<10:
    print("x")
    i += 1
print("y")    

while True:
    print("x")
    break

print("********************")

#i+=1 koymayı unutma while da
i = 0
while i < len(krediler):
    print(krediler[i])
    i += 1
print("************")

#konut kredisine gelince yazmadan kırar
i = 0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i += 1

#yukarıdaki kodun sıralamasına göre senaryolar değişir o yüzden bu sıralamyı değiştirerek dene

print("*****************************************")


#fonksiyonlar

fiyat = 100
indirim = 20

yeniFiyat = fiyat - indirim

yeniFiyat2 = fiyat - 20

yeniFiyat3 = fiyat - 20


#defination define 

def calculate ():
    print(100-20)

def calculateWithParams(fiyat,indiirm):
    print(fiyat-indirim)

def sayHello(name):
    print(f"merhaba {name}")    

calculate()
calculateWithParams(50,10)
calculateWithParams(100,25)
sayHello("HAKAN")
sayHello("sevgi")
sayHello("DURSUN ALİ")




def calculateAndReturn (price,discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)































