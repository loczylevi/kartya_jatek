pakli_kartya = [0,1,2,3,4,5,6,7,8,9,10]
import random
pakli_kartya2 = []

for elem in pakli_kartya:
    elem = str(elem)
    pakli_kartya2.append(elem)
    
print(f"Eredeti kártya pakli: {', '.join(pakli_kartya2)}\n")

#pakli kártya keverő program _______________________________________

def kevero(pakli, hanyszor_keverjen):
    a = 0
    while a <= hanyszor_keverjen:
        index = random.randint(0,len(pakli)-1)
        kivalasztott = pakli[index]
        pakli.pop(index)
        index = random.randint(0,len(pakli)-1)
        pakli.insert(index, kivalasztott)
        a = a + 1
    return pakli

#__________________________________________________________________

hanyszor_keverjunk = int(input("Hányszor keverjük meg a kártya paklit?\t"))

print(f"Megkevert kártya pakli: {' ,'.join(kevero(pakli_kartya2, hanyszor_keverjunk))}")






