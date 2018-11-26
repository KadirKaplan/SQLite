import sqlite3




baglanti = sqlite3.connect("ogrenciler.db")
isaretci = baglanti.cursor()

def tablo_olustur():


    isaretci.execute("create table if not exists ogrenciler(isim TEXT , soyad TEXT , Dogum_Tarihi INT)")
    baglanti.commit()

def tablo_veri_ekle(isim,soyad,dogum_tarihi):
    isaretci.execute("insert into ogrenciler values ('{}','{}',{})".format(isim,soyad,dogum_tarihi))
    baglanti.commit()


def tablo_veri_Cek():
    isaretci.execute("select * from ogrenciler")
    veriler=isaretci.fetchall()
    print (veriler)
    for i in veriler:
        print (i)



def guncelle(yeniIsim,eskiIsim):
    isaretci.execute("update ogrenciler set isim = '{}' where isim = '{}' ".format(yeniIsim,eskiIsim))

    baglanti.commit()


def sil(isim):
    isaretci.execute("delete from ogrenciler where isim = '{}'".format(isim))
    baglanti.commit()

tablo_olustur()


secim=raw_input("Veri eklemek icin 1'e, Veri guncellemek icin 2'e,Veri Silmek icin 3'e,cikmak icin 'q' basiniz!")

if secim == '1':
        isim=raw_input("isim ?:")
        soyad=raw_input("soyad ?:")
        dogum_tarihi=int(input("tarih ?:"))
        tablo_veri_ekle(isim,soyad,dogum_tarihi)


elif secim == '2':

        yeniIsim=raw_input("yeni isim giriniz:")
        eskiIsim=raw_input("eski isim gir2iniz:")

        guncelle(yeniIsim,eskiIsim)

elif secim=='3':
    isim=raw_input("Silmek istediginiz ismi giriniz:")
    sil(isim)
elif secim =='q':
    quit()


#tablo_veri_Cek()

baglanti.close()
