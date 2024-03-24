class personel:
    def __init__(self, ad, departman, cal_yil, maas):
        self.ad = ad
        self.departman = departman
        self.cal_yil = cal_yil
        self.maas = maas

class firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("\nAdı :", personel.ad)
            print("Departman:", personel.departman)
            print("Çalışma yılı:", personel.cal_yil)
            print("Maaş:", personel.maas)

    def maaş_zammı(self, personel, zam_oranı):
        personel.maas = personel.maas+personel.maas*(zam_oranı / 100)

    def personel_çıkart(self, personel):
        self.personel_listesi.remove(personel)


personel1 = personel("Ahmet", "A", 5, 5000)
personel2 = personel("Mehmet", "B", 3, 4500)
personel3 = personel("Ayşe", "C", 2, 4000)


print("Personeller\n")
firma = firma()
firma.personel_ekle(personel1)
firma.personel_ekle(personel2)
firma.personel_ekle(personel3)

firma.personel_listele()

firma.maaş_zammı(personel1,10)
print("\npersonelin maaşına %10 zaam yapıldı: ",personel1.maas)

firma.personel_çıkart(personel2)
print("\nKalan personeller:")
firma.personel_listele()
