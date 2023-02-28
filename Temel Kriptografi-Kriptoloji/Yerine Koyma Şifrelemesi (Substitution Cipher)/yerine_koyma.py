def yerine_koyma_sifre(acik_metin):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    anahtar = 'müfıvejihpğaodyrubşgzcötsçlnk'
    yerine_koy = {}
    for i in range(len(alfabe)):
        yerine_koy[alfabe[i]] = anahtar[i]

    sifreli_metin = ''
    for karakter in acik_metin:
        if karakter.lower() in alfabe:
            sifreli_metin += yerine_koy[karakter.lower()].upper() if karakter.isupper() else yerine_koy[karakter.lower()]
        else:
            sifreli_metin += karakter

    return sifreli_metin
