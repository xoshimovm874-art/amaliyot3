import json

with open("sozlamalar.json", "r", encoding="utf-8") as fayl:
    sozlamalar = json.load(fayl)

mavzu = input("Mavzu (light/dark): ")
bildirishnoma = input("Bildirishnoma (ha/yo'q): ")

sozlamalar["mavzu"] = mavzu

if bildirishnoma == "ha":
    sozlamalar["bildirishnoma"] = True
else:
    sozlamalar["bildirishnoma"] = False

with open("sozlamalar.json", "w", encoding="utf-8") as fayl:
    json.dump(sozlamalar, fayl, indent=4, ensure_ascii=False)

print("Sozlamalar yangilandi!")
