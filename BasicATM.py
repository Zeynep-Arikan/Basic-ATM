#BANKAMATIK UYGULAMASI

Musteri1Hesap = {
    'ad': 'Zeynep Arıkan',
    'hesapNo': '12354',
    'bakiye': 3000,
    'ekHesap': 2000,
    
}

Musteri2Hesap = {
    'ad': 'Ali saygın',
    'hesapNo': '5478',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>= miktar):
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı?(e/h)')

            if ekHesapKullanimi =='e':
                bakiye = hesap['bakiye']

                kullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= kullanilacakMiktar
                print('paranızı çekebilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']}nolu hesabınızda {hesap['bakiye']} türk lirası bulunmaktadır")
                print('Bankamatikteki işleminiz sona ermiştir.')
        else:
            print('yetersiz bakiye')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} lira bulunmaktadır.Ek hesap limitiniz ise {hesap['ekHesap']} dır.")


def paraYatirma(hesap):
    print(f"Merhaba {hesap['ad']} ")
    paraYatir = input('Para yatırmak ister misiniz?(evet ya da hayır yazın)')
    if paraYatir == 'evet':
        tutar = int(input("Ne kadar para yatırmak istiyorsunuz: "))
        hesap['bakiye'] = hesap['bakiye'] + tutar
        print(f" yeni bakiyeniz {hesap['bakiye']}")
    else:
        print('Bankamatikteki işleminiz sona ermiştir.')


paraCek(Musteri1Hesap, 3000)
bakiyeSorgula(Musteri1Hesap)
print('*******')
paraCek(Musteri1Hesap, 2000)
bakiyeSorgula(Musteri1Hesap)
print('--------------')
paraYatirma(Musteri1Hesap)
bakiyeSorgula(Musteri1Hesap)
