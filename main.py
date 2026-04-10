def titkosit_komplex(szoveg, jelszo):
    # Ebbe a listába gyűjtjük a titkosított számokat
    titkositott = []
    
    # Az előző titkosított értéket tárolja,
    # hogy a következő karakter számításába is beleszóljon
    elozo = 0

    # Végigmegyünk a szöveg minden karakterén
    # i = index, c = aktuális karakter
    for i, c in enumerate(szoveg):
        # Az aktuális karakter Unicode száma
        s = ord(c)
        
        # A jelszó megfelelő karakterének Unicode száma
        # i % len(jelszo) miatt a jelszó körbeismétlődik
        k = ord(jelszo[i % len(jelszo)])
        
        # A titkosítás lényege:
        # - az aktuális karakter száma
        # - a jelszó karakterének száma
        # - az aktuális index (0-255 között)
        # - az előző titkosított érték
        # XOR művelettel összekeverve
        uj = (s ^ k ^ (i % 256) ^ elozo) % 256
        
        # Szövegként eltároljuk a kapott számot
        titkositott.append(str(uj))
        
        # Elmentjük az aktuális értéket a következő körhöz
        elozo = uj

    # A titkosított számokat "-" jellel összefűzve adjuk vissza
    return "-".join(titkositott)


def visszafejt_komplex(titkositott_szoveg, jelszo):
    # Ebbe építjük vissza az eredeti szöveget
    vissza = ""
    
    # A "-" mentén feldaraboljuk a titkosított számsorozatot
    szamok = titkositott_szoveg.split("-")
    
    # Kezdetben nincs előző titkosított érték
    elozo = 0

    # Végigmegyünk az összes titkosított számon
    for i, n in enumerate(szamok):
        # Az aktuális titkosított szám egész számmá alakítva
        t = int(n)
        
        # A jelszó megfelelő karakterének Unicode száma
        k = ord(jelszo[i % len(jelszo)])
        
        # Ugyanazzal a logikával visszafejtjük az eredeti karaktert
        # Itt fontos, hogy az 'elozo' az előző TITKOSÍTOTT szám legyen
        uj = (t ^ k ^ (i % 256) ^ elozo) % 256
        
        # A visszakapott számból karaktert csinálunk
        vissza += chr(uj)
        
        # Következő körhöz eltároljuk a mostani titkosított számot
        elozo = t

    # Visszaadjuk a visszafejtett szöveget
    return vissza


# -------------------------
# Teszt az ellenőrzéshez
# -------------------------

# Az eredeti szöveg, amit titkosítani szeretnénk
eredeti = "Szupertitkos üzenet!"

# A titkosításhoz használt jelszó
jelszo = "ujjelszo456"

# Titkosítás
titkositott = titkosit_komplex(eredeti, jelszo)
print("Titkosított:", titkositott)

# Visszafejtés
vissza = visszafejt_komplex(titkositott, jelszo)
print("Visszafejtett:", vissza)
