import random
import time
zivoty = 10
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

            # Check if the player's health exceeds the maximum
            if zivoty > 5:
                zivoty = 5  # Set it to the maximum health
        elif volba == "meč":
            utok_mece = random.randint(1, 4)
            print(f"Zasadil jsi prasopsovi úder mečem se silou {utok_mece}.")
            zivoty_prasopes -= utok_mece
        else:
            print("Neplatná volba. Přišel jsi o příležitost na útok")

        utok_prasopes = random.randint(1, 5)
        print(f"Prasopes tě zaútočil s silou {utok_prasopes}.")
        zivoty -= utok_prasopes

        time.sleep(1)

    if zivoty <= 0:
        print("Bohužel, prasopes tě porazil. Konec hry.")
    else:
        print("Gratulujeme, porazil jsi ohromného prasopsa!")
boss_fight()