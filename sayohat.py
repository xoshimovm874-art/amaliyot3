import math

shaharlar = {"A": (0, 0), "B": (3, 4), "C": (6, 0)}

def masofa(nuqta1, nuqta2):
     x1, y1 = nuqta1
     x2, y2 = nuqta2
     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 )
 
eng_uzoq = 0
juftlik = () 

nomlar = list(shaharlar.keys())

for i in range(len(nomlar)):
    for j in range(i + 1, len(nomlar)):
        shahar1 = nomlar[i]
        shahar2 = nomlar[j]
        
        natija = masofa(shaharlar[shahar1], shaharlar[shahar2])
    
        print(shahar1, "-", shahar2, ":", natija)
        
        if natija > eng_uzoq:
            eng_uzoq = natija
            juftlik =(shahar1,shahar2)
        
        
print("eng uzoq juftlik", juftlik)
print("masofa", eng_uzoq)