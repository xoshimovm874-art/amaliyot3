tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

yangi = []

barchasida = tadbir_1 & tadbir_2 & tadbir_3
print("Barcha tadbirlarda:", ", ".join(sorted(barchasida)))

for son in tadbir_1 | tadbir_2 | tadbir_3:
    soni = sum(son in royxat for royxat in (tadbir_1, tadbir_2, tadbir_3))

    if soni == 1 and son not in yangi:
        yangi.append(son)
print("Faqat bittasid bori", yangi)


kamida_ikkita = []

for son in tadbir_1 | tadbir_2 | tadbir_3:
    jami = (son in tadbir_1) + (son in tadbir_2) + (son in tadbir_3)

    if jami >= 2:
        kamida_ikkita.append(son)
print("Kamida ikkitasida borlari", kamida_ikkita)

