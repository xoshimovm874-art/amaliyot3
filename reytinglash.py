natijalar = [
    {"ism": "Aziza", "ball": 82},
    {"ism": "Jasur", "ball": 64},
    {"ism": "Madina", "ball": 91},
    {"ism": "Sardor", "ball": 70}
]

yuqori = list(filter(lambda oquvchi: oquvchi["ball"] > 70, natijalar))
print(yuqori)

oshirilgan = list(map(lambda oquvchi:oquvchi["ball"] * 1.1, 1), natijalar)
print("10% oshirilgan ballar:", oshirilgan)

saralangan = sorted(natijalar, key=lambda oquvchi: oquvchi["ball"], reverse=True)
print("Saralangan:", ", ".join(map(lambda oquvchi: oquvchi["ism"], saralangan)))