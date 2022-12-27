import random
class AsalSayiBulABC:
    def __init__(self,_Nektar_Sayisi,_Parametre_Sayisi,_Limit,_Alt_Sinir,_Ust_Sinir,_Dongu_Boyutu):
        self.durum=False
        self.Dongu=0;
        self.Dongu_Boyutu=_Dongu_Boyutu
        self.Nektar_Sayisi=_Nektar_Sayisi
        self.Nektarlar=[];
        self.parametre_sayisi=_Parametre_Sayisi;
        self.Alt_Sinir=_Alt_Sinir;
        self.Ust_Sinir=_Ust_Sinir;
        self.en_iyi_nektar=[]
        self.toplam_fitness=0;
       
    class Nektar:
        def __init__(self):
            self.parametreler=[]
            self.Fitness=0;
            self.secilme_olasiligi=0;
            self.Limit=0;
        
    def parametre_olustur(self):
        parametreler=[]
        for x in range(self.parametre_sayisi):
            parametreler.append(int(random.random()*(self.Alt_Sinir-self.Ust_Sinir)+self.Alt_Sinir))
        return parametreler;
            
    def Nektar_olustur(self):
        for x in range(self.Nektar_Sayisi):
            self.Nektarlar.append(self.Nektar())
            self.Nektarlar[x].parametreler=self.parametre_olustur()
            asal_sayi_miktarı=self.asal_sayisi_hesapla(self.Nektarlar[x]);
            self.Nektarlar[x].Fitness=self.fitness_hesapla(asal_sayi_miktarı);
        self.olasilik_hesaplama();
            
    def olasilik_hesaplama(self):
        for x in range(self.Nektar_Sayisi):
            self.toplam_fitness+=self.Nektarlar[x].Fitness
        for y in range(self.Nektar_Sayisi):
            self.Nektarlar[y].secilme_olasiligi=self.Nektarlar[y].Fitness/self.toplam_fitness

    def asal_sayisi_hesapla(self,nektar):
        sayi=0;
        for x in range(self.parametre_sayisi):
            if(self.asal_kontrol(nektar.parametreler[x])):
                sayi+=1;
        return sayi;
        

    def fitness_hesapla(self,asal_sayi_miktarı):
        return (1 / (asal_sayi_miktarı + 1))
        
            
    def asal_kontrol(self, sayi):
        asalDurum=False;
        if sayi > 1:
           for i in range(2,sayi):
            if (sayi % i) == 0:
                asalDurum=False;
                break
            else:
                asalDurum=True;
        else:
            asalDurum=False;
        return asalDurum;

    def Isci_Ari_Fazi(self):
        i=0;
        while(i<self.Nektar_Sayisi):# Tüm Nektarlar İçin Komşu Nektar Üretimi
            _degisecekParametre_index=int(random.random()*self.parametre_sayisi)
            komsu_nektar_index=int(random.random()*self.Nektar_Sayisi)
            degisecekParametre=self.Nektarlar[i].parametreler[_degisecekParametre_index]
            komsuParametre=self.Nektarlar[komsu_nektar_index].parametreler[_degisecekParametre_index]
            yeni_parametre_degeri=int(degisecekParametre+random.uniform(-1,1)*(degisecekParametre-komsuParametre))
            if(yeni_parametre_degeri>self.Ust_Sinir):
                yeni_parametre_degeri=self.Ust_Sinir
            elif(yeni_parametre_degeri<self.Alt_Sinir):
                yeni_parametre_degeri=self.Alt_Sinir
            gecici_nektar=self.Nektar()
            gecici_nektar.parametreler=self.Nektarlar[i].parametreler.copy()
            gecici_nektar.parametreler[_degisecekParametre_index]=yeni_parametre_degeri;
            gecici_nektar.Fitness=self.fitness_hesapla(self.asal_sayisi_hesapla(gecici_nektar))
            if(self.Nektarlar[i].Fitness>gecici_nektar.Fitness):
                self.Nektarlar[i].parametreler=gecici_nektar.parametreler.copy()
                self.Nektarlar[i].Fitness=gecici_nektar.Fitness
            else:
                self.Nektarlar[i].Limit+=1 
            print(self.Nektarlar[i].Limit) 
            i=i+1
    
    def Gozcu_Ari_Fazi(self):
        i=0;
        while(i<self.Nektar_Sayisi):# Tüm Nektarlar İçin Komşu Nektar Üretimi
            print("deneem")
            i+=1
    
    def Dongu_Say(self):
        self.Dongu+=1
        self.durum=bool(self.Dongu >= self.Dongu_Boyutu)

    def main(self):
        self.Nektar_olustur();
        while(not(self.durum)):
            self.Isci_Ari_Fazi();
            self.olasilik_hesaplama();
            self.Gozcu_Ari_Fazi();
            #self.En_iyi_belirleme();
            #self.Kasif_Ari_Fazi();
            self.Dongu_Say();
            print("dongu saydık")

    print("Başladı")


Go=AsalSayiBulABC(10,4,0,100,150,10);
Go.main();


