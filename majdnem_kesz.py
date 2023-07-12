
pakli_kartya = ["P-0","P-1","P-2","P-3","P-4","P-5","P-6","P-7","P-8","P-9","Z-0","Z-1","Z-2","Z-3","Z-4","Z-5","Z-6","Z-7","Z-8","Z-9","K-0","K-1","K-2","K-3","K-4","K-5","K-6","K-7","K-8","K-9","S-0","S-1","S-2","S-3","S-4","S-5","S-6","S-7","S-8","S-9"]
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
print(len(pakli_kartya2))
hanyszor_keverjunk = int(input("Hányszor keverjük meg a kártya paklit?\t"))

print(f"Megkevert kártya pakli: {' ,'.join(kevero(pakli_kartya2, hanyszor_keverjunk))}")

#print(f"\n{pakli_kartya2}")

megkevert = kevero(pakli_kartya2, hanyszor_keverjunk)




jatekos = []

bot = []

#pakli kártya osztó program _______________________________________

kezdo_lap = megkevert[0]
megkevert.pop(0)

def oszto(megkevert_pakli):
    for szam in range(5):
        tarolo = megkevert_pakli[szam]
        megkevert_pakli.pop(szam)
        jatekos.append(tarolo)
    for szam in range(5):
        tarolo = megkevert_pakli[szam]
        megkevert_pakli.pop(szam)
        bot.append(tarolo) 
    return bot, jatekos

#__________________________________________________________________


print("________________________________________________-")
print(oszto(megkevert))
print(len(pakli_kartya2))

while True:
    if len(megkevert) == 0:
        megkevert = kevero(pakli_kartya2, 1000)
    if len(bot) == 0:
        print("vege a bot nyert")
        break
    if len(jatekos) == 0:
        print("vege a jatekos nyert")
        break
    
    print(f"A te lapjaid: {jatekos}")
    print(f"pakil lapok száma: {len(megkevert)} db.")
    print()
    print(f"kezdó lap: {kezdo_lap}")
    print("INFO: ha nem akarsz lapot lerakni nyomj entert!")
    bekeres = input("melyik lapodat rakod le?\t")
    skipp = False
    if bekeres == "":
        skipp = True
    try:
        if bekeres == "":
            tarolo3 = megkevert[0]
            megkevert.pop(0)
            jatekos.append(tarolo3)
        if skipp == False:
            if bekeres in jatekos:
                for lap in jatekos:
                    if bekeres[0] == lap[0] or bekeres[2] == lap[2]:
                        kezdo_lap = bekeres
                        jatekos.remove(bekeres)
                        break
                    
                    else:
                        print("nincs olyan kártya a kezedben amit le tudnál rakni")
                    
                
        
            else:
                print("nincs ilyen lapod a kezedben")
            
        
    except:
        print("valami nem jó gec")
        
        
        
    # jön a bot
    print("jon a bot_____________________________________\n")
    print(f"A bot lapjai: {bot}")
    print(f"pakil lapok száma: {len(megkevert)} db.")
    print()
    print(f"kezdó lap: {kezdo_lap}")
    volt_e = False
    for lap in bot:
        if kezdo_lap[0] == lap[0] or kezdo_lap[2] == lap[2]:
            kezdo_lap = lap
            bot.remove(lap)
            volt_e = True
            break
    if volt_e == False:
        tarolo5 = megkevert[0]
        megkevert.pop(0)
        bot.append(tarolo5)
        
        
            

    
        
        
    
    
    



