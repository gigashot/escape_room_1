import time
import random

print("Vítejte v dobrodružné hře!")
print("Jsi v labyrintu a máš na výběr ze tří chodeb.")
zivoty = 3  # Počáteční počet životů

def vyber_chodby():
    global zivoty  # Použití globalu pro změnu hodnoty v globálním rozsahu
    
    while True:
        print("1. chodba levá")
        print("2. chodba prostřední")
        print("3. chodba pravá")

        vyber = input("Zvolte cestu (1/2/3): ")

        if vyber == "1":
            print("procházíte tajemnou chodbou...")
            time.sleep(2)
            print("Narazíte na místnost, ve které sedí zelený skřet.")
            print("Skřet vás vyzývá na soutěž v kostkách.")
            vyber_hry_kostek = input("přijmte jeho nabídku? (1/2): ")
            
            if vyber_hry_kostek == "1":
                hrdina_kostka = random.randint(2, 6)
                print("házej první...")
                time.sleep(1)
                print("kostka se kutálí")
                time.sleep(1)
                print(f"kostka se přetočila, a máš: {hrdina_kostka}")

                skret_kostka = random.randint(1, 5)
                time.sleep(1)
                print("teď hází skřet")
                time.sleep(1)
                print(f"kostka se přetočila, a je to {skret_kostka}")
                
                # Upraveno pro aktualizaci hodnoty životů
                if skret_kostka > hrdina_kostka:
                    zivoty -= 1
                    print(f"ztrácíš 1 život, už ti zbývají jen {zivoty} životy")
                elif skret_kostka < hrdina_kostka:
                    zivoty += 1
                    print("skřet vypadá velice nezpokojeně")
                    time.sleep(1)
                    print(f"získáváš 1 život, už máš {zivoty} životy")
                else:
                    print("nikdo nevyhrává, skřet tě pouští dál")
                break
            else:
                print("Rozhodl jsi se neúčastnit se soutěže. Skřet tě bodne kudlou do břicha a umíráš")
                print("prohrál jsi hru")
                break
        else:
            print("Neplatná volba. Zkuste to znovu.")
        time.sleep(1)
        print("po setkání se skřetem jsipokračoval dál, ven z místnosti chodbou do další místnosti") 
        time.sleep(1)
        print("zde potkáváš moudrého čaroděje který chce abys uhodnul číslo které si myslí")
        print("Skřet vás vyzývá na soutěž v kostkách.")
        vyber_hadani_cisla = input("přijmte jeho nabídku? (1/2): ")
        if vyber_hadani_cisla ==1:
            print("sumting")
        else:
            time.sleep(1)
            print("Čaroděj vyvolal mocnou kledbu a usmrtil tě.")
            time.sleep(1)
            print("konec hry")
            break

            
vyber_chodby()