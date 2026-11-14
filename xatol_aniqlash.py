def bolish(a, b):
    assert b != 0, "Nolga bo‘lish mumkin emas."
    return a / b


try:
    son1 = float(input("Birinchi son: "))
    son2 = float(input("Ikkinchi son: "))

    natija = bolish(son1, son2)
    print("Natija:", natija)

except ValueError:
    print("Xatolik: Son o‘rniga matn kiritildi.")

except AssertionError as xatolik:
    print("Xatolik:", xatolik)
    print("Dastur ishlashda davom etmoqda.")