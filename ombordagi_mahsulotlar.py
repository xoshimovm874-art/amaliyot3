ombor_1 = {"olma": 20, "anor": 12, "nok": 8}
ombor_2 = {"olma": 15, "banan": 10, "nok": 5}

qoshish = {}

for mahsulot in ombor_1:
    qoshish[mahsulot] = ombor_1[mahsulot]
    
for mahsulot in ombor_2:
    if mahsulot in qoshish:
        qoshish[mahsulot] += ombor_2[mahsulot]
    else:
        qoshish[mahsulot] = ombor_2[mahsulot]
        
print(qoshish)