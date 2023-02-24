def sezar_hack(sifreli_metin):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    for anahtar in range(1,29):
        cozulmus_metin = ''
        for harf in sifreli_metin:
            if harf.lower() in alfabe:
                index = alfabe.index(harf.lower())
                otelenmis_index = (index - anahtar) % len(alfabe)
                if harf.isupper():
                    cozulmus_metin += alfabe[otelenmis_index].upper()
                else:
                    cozulmus_metin += alfabe[otelenmis_index]
            else:
                cozulmus_metin += harf
        print(f"Anahtar {anahtar}: {cozulmus_metin}")
