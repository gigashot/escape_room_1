import time
import random

print("Vítejte v dobrodružné hře!")
print("Jsi v labyrintu a máš na výběr ze tří chodeb.")
zivoty = 5  # Počáteční počet životů

nemoc_hrdina = [""]


def vyber_chodby():
    global zivoty  # Použití globalu pro změnu hodnoty v globálním rozsahu
    
    while True:
        print("1. chodba levá")
        print("2. chodba prostřední")
        print("3. chodba pravá")

        vyber = input("Zvolte cestu (1/2/3): ")
        if vyber == "3":
            print("vybral jste si pravou cestu")
            time.sleep(1)
            print("slyšíte hlasité hřmění")
            time.sleep(1)
            print("chodba se hroutí")
            time.sleep(1)
            print("zasypaly vás sutiny chodby")
            time.sleep(1)
            print("konec hry")
            return
        if vyber == "2":
            print("procházíte prostřední chodbou...")
            time.sleep(1)
            print("Narazíte na místnost, ve které jsou před vámi 3 dveře.")
            time.sleep(1)
            print("vyberte právě ty dveře za kterými máte nejvyšší šanci přežít")
            time.sleep(1)
            print("1. za prvními dveřmi je komora plná jedovatého plynu, který na kontakt leptá kůži a rozkládá živou tkáň")
            time.sleep(1)
            print("2. za druhými dveřmi je místnost se smečkou agresivních prasopsů kteří už měsíc nic nejedli ")
            time.sleep(1)
            print("3. za třetími dveřmi je místnost plná tisíců krvežíznivích komárů nakaženi malárií.")
            time.sleep(1)
            vyber_dvere = input("do jakých dveří se vydáte (1/2/3)")
            if vyber_dvere == "1":
                print("vešel jste do komory s plynem, skoro okamžitě ztrácíte vědomí...")
                time.sleep(1)
                print("umíráte...")
                time.sleep(1)
                print("konec hry")
                return
            elif vyber_dvere == "2":
                zivoty = zivoty + 8
                print("vešel jste do místnosti s agresivními prasopsy ...")
                time.sleep(1)
                print("vidíte kolem sebe páchoucí mrtvoly 8 prasopsů...")
                time.sleep(1)
                print("dostáváte 8 hp navíc, za každého prasopsa")
                time.sleep(1)
                print("pokračujete do další místnosti")
                boss_fight()
                return

            elif vyber_dvere == "3":
                print("vstoupil jste do místnosti plné komáry nakaženi malárií.")
                time.sleep(1)
                print("stovky komárů vás ihned poštípali, máte 24 hodin než umřete")
                nemoc_hrdina.append ("malarie")
                time.sleep(1)
                malarie_rozhodnuti = input("chcete pokračovat do dalších dveří - 1, nebo přijmout svoji smrt - 2.")
                if malarie_rozhodnuti == "1":
                    boss_fight()
                    return
                elif malarie_rozhodnuti == "2":
                    print("umíráte po 24 hodinách, celý od své vlastní krve a poštípaný komáry.")
                    print("konec hry")
                    return
                else:
                    print("neplatný vstup.")

                            
        if vyber == "1":
            print("procházíte tajemnou chodbou...")
            time.sleep(1)
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
                    print("skřet vypadá velice nespokojeně")
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
    print("po setkání se skřetem jsi pokračoval dál, ven z místnosti chodbou do další místnosti") 
    time.sleep(1)
    print("zde potkáváš moudrého čaroděje který chce s vámi hrát hru.")
    time.sleep(2)
    print("Čaroděj chce hrát hru abys uhodnul číslo od které si myslí.")
    time.sleep(1)

    vyber_hadani_cisla = input("přijmete jeho nabídku? (1/2): ")
    if vyber_hadani_cisla == "1":
        print("přijmul jsi jeho nabídku")
        time.sleep(1)
        print(f"hádej číslo od 1 do  10, máš na to {zivoty} pokusy,")
        time.sleep(1)
        print("každý pokus odpovídá 1 tvému životu")
        time.sleep(1)
        skryte_cislo = random.randint(1, 10)
        while zivoty > 0 or skryte_cislo == cislo_tip:
            try:
                time.sleep(1)
                cislo_tip = int(input("Zadejte váš tip od 1 do 10: "))
            except ValueError:
                time.sleep(1)
                print("Chyba: Zadejte platné celé číslo.")
                continue

            if cislo_tip == skryte_cislo:
                time.sleep(1)
                print("Gratulujeme! Uhádli jste číslo.")
                zivoty = zivoty + 10
                boss_fight()
                break
            elif cislo_tip < skryte_cislo:
                print("Tip je příliš malý.")
                zivoty -= 1
            elif cislo_tip > skryte_cislo:
                print("Tip je příliš velký.")
                zivoty -= 1
                time.sleep(1)
                print(f"Zbývající životy: {zivoty}")

            if zivoty == 0:
                time.sleep(1)
                print(f"Bohužel jste vyčerpal/a všechny životy. Skryté číslo bylo {skryte_cislo}.")
                print("konec hry")
                break
    else:
        time.sleep(1)
        print("Čaroděj se rozzuřil a proměnil vás v bramboru.")    
        time.sleep(1)
        print("konec hry")
        return
def boss_fight():
    print("Vítej v posledním souboji! Čelíš ohromnému prasopsovi.")
    global zivoty
    zivoty_prasopes = 15

    while zivoty > 0 and zivoty_prasopes > 0:
        print(f"\nZbývá ti {zivoty} životů. Prasopes má {zivoty_prasopes} životů.")
        volba = input("Co uděláš? (heal/meč): ").lower()

        if volba == "heal":
            heal_sila = random.randint(2, 5)
            print(f"Vyléčili jste si {heal_sila} hp.")
            zivoty += heal_sila
        elif volba == "meč":
            utok_mece = random.randint(1, 4)
            print(f"Zasadil jsi prasopsovi úder mečem se silou {utok_mece}.")
            zivoty_prasopes -= utok_mece
        else:
            print("Neplatná volba. přišel jsi o příležitost na útok")

       
        utok_prasopes = random.randint(1, 5)
        print(f"Prasopes tě zaútočil s silou {utok_prasopes}.")
        zivoty -= utok_prasopes

        time.sleep(1)

    if zivoty <= 0:
        print("Bohužel, prasopes tě porazil. Konec hry.")
        if "malarie" in nemoc_hrdina:
            print("ale na tom stejně nesejde, protože by jste do 23 hodin umřeli na Malárii ")
        return
    
    else:
        print("Gratulujeme, porazil jsi ohromného prasopsa !")
        if "malarie" in nemoc_hrdina:
            print("ale na tom stejně nesejde, protože umřete do 23 hodin na Malárii ")
        return
    
vyber_chodby()
