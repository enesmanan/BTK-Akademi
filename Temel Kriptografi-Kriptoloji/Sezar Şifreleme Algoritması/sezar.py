def sezar_sifre(metin, anahtar=3):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    sifreli_metin = ''
    for harf in metin:
        if harf in metin:
            index = alfabe.index(harf.lower())
            otelenmis_index = (index + anahtar) % len(alfabe)
            if harf.isupper():
                sifreli_metin += alfabe[otelenmis_index].upper()
            else:
                sifreli_metin += alfabe[otelenmis_index]
        else:
            sifreli_metin += harf
    return sifreli_metin 

