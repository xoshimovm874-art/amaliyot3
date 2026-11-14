with open("ish_vaqti.txt", "r", encoding="utf-8") as f:
    malumot = f.read().split()

jami = 0
xodimlar = {}

for i in range(0, len(malumot), 2):
    ism = malumot[i]
    soat = malumot[i + 1]

    try:
        soat = int(soat)
        jami += soat
        xodimlar[ism] = soat

    except ValueError:
        print(f"Ogohlantirish: {ism} uchun soat qiymati noto‘g‘ri.")

eng_kop = max(xodimlar, key=xodimlar.get)

print("Jami ish soati:", jami)
print(f"Eng ko‘p ishlagan: {eng_kop} — {xodimlar[eng_kop]} soat")