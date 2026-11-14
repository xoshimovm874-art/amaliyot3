
import csv

kategoriyalar = {}

with open("savdo.csv", "r", encoding="utf-8") as fayl:
    oqish = csv.DictReader(fayl)

    for qator in oqish:
        kategoriya = qator["kategoriya"]
        narx = int(qator["narx"])
        miqdor = int(qator["miqdor"])

        tushum = narx * miqdor

        if kategoriya in kategoriyalar:
            kategoriyalar[kategoriya] += tushum
        else:
            kategoriyalar[kategoriya] = tushum

for kategoriya, summa in kategoriyalar.items():
    print(f"{kategoriya}: {summa:,} so'm".replace(",", " "))

eng_daromadli = max(kategoriyalar, key=kategoriyalar.get)

print(f"Eng daromadli kategoriya: {eng_daromadli}")
