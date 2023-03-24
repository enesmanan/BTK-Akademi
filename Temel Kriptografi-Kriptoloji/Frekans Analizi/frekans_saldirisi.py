import codecs

sirali_frekans = ['a', 'e', 'i', 'r', 'l', 'ı', 'd', 'k', 'n', 'm', 'y', 'u', 's', 't', 'b', 'o', 'ü', 'ş', 'z', 'g', 'h', 'ç', 'ğ', 'c', 'v', 'p', 'ö', 'f', 'j']

def dosya_oku(dosya_adi):
    with codecs.open(dosya_adi, 'r', 'utf-8') as dosya:
        icerik = dosya.read()
    return icerik

def dosya_yaz(dosya_adi, icerik):
    with codecs.open(dosya_adi, 'w', 'utf-8') as dosya:
        dosya.write(icerik)

def frekans_analizi(metin):
    frekans = {}
    for harf in metin:
        if harf in frekans:
            frekans[harf] += 1
        else:
            frekans[harf] = 1
    return frekans

def en_yuksek_frekansli_harfler(frekans, harfler='abcçdefgğhıijklmnoöprsştuüvyz'):
    sirali_frekans = sorted(frekans.items(), key=lambda x: x[1], reverse=True)
    en_yuksek_harfler = []
    for harf, sayi in sirali_frekans:
        if harf in harfler:
            en_yuksek_harfler.append(harf)
    return en_yuksek_harfler

def sifre_coz(metin, sirali_frekans, en_yuksek_harfler):
    sifreli_metin = metin
    for i in range(len(en_yuksek_harfler)):
        sifreli_metin = sifreli_metin.replace(en_yuksek_harfler[i], sirali_frekans[i])
    return sifreli_metin

if __name__ == '__main__':
    print(sirali_frekans)
    icerik = dosya_oku('sifreli_metin.txt')
    frekans = frekans_analizi(icerik)
    en_yFrekans = en_yuksek_frekansli_harfler(frekans)
    print(en_yFrekans)

    cozulmus_metin = sifre_coz(icerik, sirali_frekans, en_yFrekans)
    print(cozulmus_metin)

    dosya_yaz('cozulmus_metin.txt', cozulmus_metin)
