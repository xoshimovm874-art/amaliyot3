buyurtmalar = [
 {"mahsulot": "Kitob", "narx": 45000, "miqdor": 2},
 {"mahsulot": "Ruchka", "narx": 5000, "miqdor": 10},
 {"mahsulot": "Sumka", "narx": 180000, "miqdor": 1}
]

eng_qimmat = 0
mahsulot_nomi = ""

for buyurtma in buyurtmalar:
    qiymat = buyurtma["narx"] * buyurtma["miqdor"]
    print(buyurtma["mahsulot"], ":", qiymat,"so'm")
    
    if qiymat > eng_qimmat:
      eng_qimmat = qiymat
      mahsulot_nomi = buyurtma["mahsulot"]
      
print("eng qimmat buyurtma:")
print(mahsulot_nomi, ":", eng_qimmat, "so'm")