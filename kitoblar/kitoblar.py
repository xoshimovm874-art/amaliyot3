
import csv
import matplotlib.pyplot as plt


def kitoblarni_oqish():
    with open("kitoblar.csv", "r", encoding="utf-8") as fayl:
        oqish = csv.DictReader(fayl)
        return list(oqish)


# 1. Barcha kitoblarni ko'rish
def kitoblarni_korish():
    kitoblar = kitoblarni_oqish()

    for kitob in kitoblar:
        print(
            f"{kitob['nom']} | {kitob['kategoriya']} | "
            f"{kitob['muallif']} | {kitob['oqilgan']} marta"
        )


def kitob_qidirish():
    nom = input("Kitob nomini kiriting: ").strip().lower()
    kitoblar = kitoblarni_oqish()

    topildi = False

    for kitob in kitoblar:
        if nom in kitob["nom"].lower():
            print(kitob)
            topildi = True

    if not topildi:
        print("Kitob topilmadi!")


def kategoriya_filtrlash():
    kategoriya = input("Kategoriyani kiriting: ").strip().lower()
    kitoblar = kitoblarni_oqish()

    topildi = False

    for kitob in kitoblar:
        if kitob["kategoriya"].strip().lower() == kategoriya:
            print(kitob)
            topildi = True

    if not topildi:
        print("Bu kategoriyada kitob topilmadi!")



def eng_kop_oqilgan():
    kitoblar = kitoblarni_oqish()

    if len(kitoblar) == 0:
        print("Kitoblar mavjud emas!")
        return

    eng_kop = max(kitoblar, key=lambda x: int(x["oqilgan"]))

    print(
        f"Eng ko'p o'qilgan kitob: "
        f"{eng_kop['nom']} — {eng_kop['oqilgan']} marta"
    )


def kategoriya_grafik():
    kitoblar = kitoblarni_oqish()
    kategoriyalar = {}

    for kitob in kitoblar:
        kategoriya = kitob["kategoriya"].strip()
        oqilgan = int(kitob["oqilgan"])

        if kategoriya in kategoriyalar:
            kategoriyalar[kategoriya] += oqilgan
        else:
            kategoriyalar[kategoriya] = oqilgan

    plt.bar(kategoriyalar.keys(), kategoriyalar.values())
    plt.title("Kategoriyalar bo'yicha o'qilish")
    plt.xlabel("Kategoriyalar")
    plt.ylabel("O'qilgan soni")
    plt.show()


def kitob_qoshish():
    nom = input("Kitob nomi: ")
    kategoriya = input("Kategoriya: ")
    muallif = input("Muallif: ")
    oqilgan = input("O'qilgan soni: ")

    if not oqilgan.isdigit():
        print("O'qilgan soni raqam bo'lishi kerak!")
        return

    yangi_kitob = {
        "nom": nom,
        "kategoriya": kategoriya,
        "muallif": muallif,
        "oqilgan": oqilgan
    }

    with open("kitoblar.csv", "a", newline="", encoding="utf-8") as fayl:
        yozish = csv.DictWriter(
            fayl,
            fieldnames=["nom", "kategoriya", "muallif", "oqilgan"]
        )
        yozish.writerow(yangi_kitob)

    print("Yangi kitob qo'shildi!")


while True:
    print("""
    1. Kitoblarni ko'rish
    2. Kitob qidirish
    3. Kategoriya bo'yicha filtrlash
    4. Eng ko'p o'qilgan kitob
    5. Grafik chiqarish
    6. Kitob qo'shish
    0. Chiqish
    """)

    tanlov = input("Tanlov: ")

    if tanlov == "1":
        kitoblarni_korish()

    elif tanlov == "2":
        kitob_qidirish()

    elif tanlov == "3":
        kategoriya_filtrlash()

    elif tanlov == "4":
        eng_kop_oqilgan()

    elif tanlov == "5":
        kategoriya_grafik()

    elif tanlov == "6":
        kitob_qoshish()

    elif tanlov == "0":
        print("Dastur tugadi!")
        break

    else:
        print("Noto'g'ri tanlov!")
