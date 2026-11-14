fayllar = ["Hisobot 2026.pdf", "profil rasmi.jpg",
           "video.mp4", "jadval.xlsx", "diagramma.png"]

yaroqli = list(filter(lambda x: x.endswith((".pdf", ".jpg", ".png")), fayllar))

yaroqli = list(map(lambda x: x.replace(" ", "_"), yaroqli))

yaroqsiz = list(filter(lambda x: not x.endswith((".pdf", ".jpg", ".png")), fayllar))

print("Yaroqli:", *yaroqli)
print("Yaroqsiz:", *yaroqsiz)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 