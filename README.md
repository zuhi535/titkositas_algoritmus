# Komplex Titkosító és Visszafejtő Python Kód

Ez a Python kód egy karakterenként működő titkosító algoritmust valósít meg **jelszó alapján**, előző karakter hatását is figyelembe véve.  
Kiváló **oktatási célokra** és **gyakorlati demonstrációra**, de **nem kriptográfiailag biztonságos**.

---

## 🔹 Tartalom

- [Elméleti háttér](#-elméleti-háttér)
- [Fő funkciók](#-fő-funkciók)
- [Folyamatábra](#-folyamatábra)
- [Használat](#-használat)
- [Tesztelés](#-tesztelés)
- [Megjegyzések](#-megjegyzések)

---

## 🔹 Elméleti háttér

- A titkosítás **XOR (^) műveletre** épül, ami visszafordítható: `A ^ B ^ B = A`.  
- Minden karakter ASCII kódja XOR-olva van a **jelszó megfelelő karakterével** és az **előző titkosított karakterrel**, így minden karakter titkosítása **függ az előzőtől** → láncolt titkosítás.  
- Ez a módszer **egyszerű, de demonstrálja a jelszófüggő titkosítás alapelvét**.

---

## 🔹 Fő funkciók

### 1️⃣ Titkosítás (`titkosit_komplex`)

- **Paraméterek:**  
  - `szoveg` – titkosítandó szöveg  
  - `jelszo` – titkosításhoz használt jelszó  

- **Működés:**  
  1. Minden karakter ASCII kódra alakítása  
  2. XOR művelet a karakter kód és a jelszó karaktere között  
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

## 🔹 Folyamatábra
                                                    Eredeti szöveg → [ASCII kódok]
                                                                │
                                                                ▼
                                                         XOR a jelszóval
                                                                │
                                                                ▼
                                                          XOR az indexszel
                                                                │
                                                                ▼
                                                    XOR az előző titkosítottal
                                                                │
                                                                ▼
                                                     Titkosított karakterek (0–255)
                                                                │
                                                 ┌──────────────┴──────────────┐
                                                 ▼                             ▼
                                          Visszafejtés ugyanazzal        Jelszó nélkül nem lehet
                                          jelszóval és XOR-logikával       visszaállítani
                                                 │
                                                 ▼
                                          Eredeti szöveg visszaállítva
---

## 🔹 Használat

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
```
## 🔹 Tesztelés

Ellenőrizd, hogy a visszafejtett szöveg megegyezik az eredetivel.

Példa kimenet:

Titkosított: 75-178-54-... (értékek jelszótól függően változnak)
Visszafejtett: Szupertitkos üzenet!

✅ Ha a visszafejtett szöveg pontosan megegyezik az eredetivel → a kód helyesen működik.

## 🔹 Megjegyzések

A titkosítás jelszófüggő, így a jelszó nélkül a visszafejtés nem lehetséges

Oktató és demonstrációs célokra alkalmas, nem biztonságos valódi adatokhoz

Minden karakter a 0–255 tartományban kerül titkosításra

Különösen alkalmas rövid szövegek titkosítására és visszafejtésére
