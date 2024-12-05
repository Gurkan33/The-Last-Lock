#Installerar simple_Colors! -----------------------------
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import simple_colors
except ImportError:
    print("simple_colors inte installerat. Installerar nu...")
    install_package("simple_colors")

#--------------------------------------------------------

import simple_colors 
import TextOchGubbar
import SystemFunktions
import Funktions
import os
import ASCII_art as ASCII
import time

os.system('cls')

print(ASCII.text("THE LAST LOCK"))

print(simple_colors.red("Welcome to The Last Lock!",["bold","underlined"]))
print(simple_colors.red("""Your now locked in a prison and have to fight your way out of it!
    Open kests, Fight enemys, Avoid traps and more! \n"""))

time.sleep(1)

player_Name = SystemFunktions.valid_character_name() #Spelare skriver in sitt namn!
Funktions.player.name = player_Name

print(simple_colors.red("Ohh! Nice name " + simple_colors.blue(str(Funktions.player.name)) + "!\n"))

print(simple_colors.red("Now ") + simple_colors.blue(str(Funktions.player.name)) + simple_colors.red(" its time to make your first move!"))

print(simple_colors.red("""What do you want to do?."""))

while True:
    if Funktions.player.hp <= 0:
        print(simple_colors.red(ASCII.text("Defeat")))
        print(f"""You died, and lost all your stuff!""")
        exit() #-------------------------------------------------------------#Dödar programmet!
    elif Funktions.player.level > 10:
        #spelare får nyckel!
        print("")

    print("""Chose what you wish to do!
    [1] Look at player info
    [2] Chose a door""")

    
    chosen_rout = input(simple_colors.blue("-->",["bold"]))
    if SystemFunktions.valid_user_choice(chosen_rout, 2, "multiChoice") == True:
        if chosen_rout == "1":
            Funktions.player_Manager()
            #print player statistics

        elif chosen_rout == "2":
            Funktions.chooseDoor()