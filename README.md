# Komplex Titkosító és Visszafejtő Python Kód

Ez a Python kód egy karakterenként működő titkosító algoritmust valósít meg jelszó alapján.  
Használata oktató és játékos célokra ideális, de **nem tekinthető kriptográfiailag biztonságosnak**.

---

## 🔹 Tartalom

- [Fő funkciók](#-fő-funkciók)
- [Használat](#-használat)

---

## 🔹 Fő funkciók

### 1️⃣ Titkosítás (`titkosit_komplex`)

- **Paraméterek:**  
  - `szoveg` – titkosítandó szöveg  
  - `jelszo` – titkosításhoz használt jelszó  

- **Működés:**  
  1. Minden karakter ASCII kódra alakítása  
  2. XOR művelet a karakter kód és a jelszó megfelelő karaktere között  
  3. Az index és az előző titkosított karakter befolyásolja az eredményt  
  4. 0–255 közé szorítás, kötőjellel elválasztott string előállítása  

- **Eredmény:** Kötőjeles string a titkosított karakterekből

---

### 2️⃣ Visszafejtés (`visszafejt_komplex`)

- **Paraméterek:**  
  - `titkositott_szoveg` – kötőjellel elválasztott titkosított string  
  - `jelszo` – titkosításhoz használt jelszó (ugyanaz, mint a titkosításnál)  

- **Működés:**  
  1. Titkosított string feldarabolása számokra  
  2. XOR művelet minden szám és a jelszó karaktere között  
  3. Az index és az előző titkosított karakter figyelembevétele  
  4. Az eredeti karakterek visszaállítása  

- **Eredmény:** Az eredeti szöveg

---

## 🔹 Használat

1. Másold a függvényeket egy Python fájlba, pl. `titkolo.py`  
2. Írd be a titkosítandó szöveget és a jelszót  
3. Hívd meg a titkosító és visszafejtő függvényeket

```python
from titkolo import titkosit_komplex, visszafejt_komplex

eredeti = "Szupertitkos üzenet!"
jelszo = "ujjelszo456"

# 🔐 Titkosítás
titkositott = titkosit_komplex(eredeti, jelszo)
print("Titkosított:", titkositott)

# 🔓 Visszafejtés
vissza = visszafejt_komplex(titkositott, jelszo)
print("Visszafejtett:", vissza)
