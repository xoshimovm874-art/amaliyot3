matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."

matn = matn.lower().replace(".", "")
sozlar = matn.split()

print("So'zlar soni:", len(sozlar))

eng_uzun = max(sozlar, key=len)
print("Eng uzun so'z:", eng_uzun)

harflar = matn.replace(" ", "")
eng_kop = max(set(harflar), key=harflar.count)
print("Eng ko'p uchragan harf:", eng_kop)

takrorlanmaydigan = []

for soz in sozlar:
    if sozlar.count(soz) == 1:
        takrorlanmaydigan.append(soz)

print("Takrorlanmaydigan so'zlar:", ", ".join(takrorlanmaydigan))
