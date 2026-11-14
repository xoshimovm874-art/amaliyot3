menu = {
      "lavash": 28000,
      "somsa": 10000,
      "choy": 5000
  }

def buyurtma(*args, **kwargs):
    jami = 0

    for mahsulot in args:
        if mahsulot in menu:
            jami += menu[mahsulot]
        else:
            print(mahsulot, "menyuda mavjud emas!")

    print("Mijoz:", kwargs["mijoz"])
    print("Telefon:", kwargs["telefon"])
    print("Jami:", jami, "so‘m")


buyurtma("lavash", "choy", "somsa",
         mijoz="Dilshod", telefon="901234567")