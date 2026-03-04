def titkosit_komplex(szoveg, jelszo):
    titkositott = []
    elozo = 0

    for i, c in enumerate(szoveg):
        s = ord(c)
        k = ord(jelszo[i % len(jelszo)])
        
        uj = (s ^ k ^ (i % 256) ^ elozo) % 256
        titkositott.append(str(uj))
        elozo = uj

    return "-".join(titkositott)


def visszafejt_komplex(titkositott_szoveg, jelszo):
    vissza = ""
    szamok = titkositott_szoveg.split("-")
    elozo = 0

    for i, n in enumerate(szamok):
        t = int(n)
        k = ord(jelszo[i % len(jelszo)])
        
        uj = (t ^ k ^ (i % 256) ^ elozo) % 256
        vissza += chr(uj)
        elozo = t

    return vissza


# teszt az ellenőrzéshez
eredeti = "Szupertitkos üzenet!"
jelszo = "ujjelszo456"

titkositott = titkosit_komplex(eredeti, jelszo)
print("Titkosított:", titkositott)

vissza = visszafejt_komplex(titkositott, jelszo)
print("Visszafejtett:", vissza)