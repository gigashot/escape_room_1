import time
import random
print("Vítejte v dobrodružné hře!")
print("Jsi v labyrintu a máš na výběr ze tří chodeb.")

while True:
    print("1. chodba levá ")
    print("2. chodba prostřední ")
    print("3. chodba pravá ")

    vyber = input("Zvolte cestu (1/2/3): ")

    if vyber == "1":
        print("procházíte tajemnou chodbou...")
        time.sleep(2)
        print("Narazíte na místnost, ve které sedí zelený skřet.")
        print("Skřet vás vyzývá na soutěž v kostkách.")
        
        vyber_hry_kostek = input("přijmte jeho nabídku ?(1/2): ")
        if vyber_hry_kostek == 1:
         hraci_kostka = random.randint(1, 6)
         print("házej první...")
         time.sleep(1)
         print("kostka se kutálí")
         time.sleep(1)
         print(f"kostka se přetočila, a je to {hraci_kostka}")

         

        break


    elif vyber == "2":
        print("Vystupujete strmou horu...")
        time.sleep(2)
        print("Na vrcholu hory objevujete poklad. Jste bohatý! Konec hry.")
        break
    elif vyber == "3":
        print("Putojete rozpálenou pouští...")
        time.sleep(2)
        print("Narazíte na oázu, kde potkáte kouzelného džina. Dává vám tři přání. Konec hry.")
        break
    else:
        print("Neplatná volba. Zkuste to znovu.")