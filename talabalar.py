import csv

yonalish = input("Yo'nalish: ")

talabalar = []
with open("talabalar.csv", "r", encoding="utf-8") as fayl:
    oqish = csv.DictReader(fayl)

    for qator in oqish:
        if qator["yonalish"] == yonalish:
            talabalar.append(qator)

talabalar.sort(key=lambda x: int(x["ball"]), reverse=True)

with open("filtrlangan_talabalar.csv", "w", newline="", encoding="utf-8") as fayl:
    ustunlar = ["ism", "yosh", "yonalish", "ball"]

    yozish = csv.DictWriter(fayl, fieldnames=ustunlar)
    yozish.writeheader()
    yozish.writerows(talabalar)

print(f"{len(talabalar)} ta talaba topildi.")
print("Natijalar filtrlangan_talabalar.csv fayliga yozildi.")
