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

Funktions.start_of_game()

level = 1
hp = 100

while True:
    if hp <= 0:
        print(simple_colors.red("Du förlorade! :(",["bold","underlined"]))
        break
    elif level > 10:
        #spelare får nyckel!
        print("")

    print("""Chose what you wish to do!
    [1] Looka at player info
    [2] Chose a door""")
    
    chosen_rout = input(simple_colors.blue("-->",["bold"]))
    if SystemFunktions.valid_user_choice(chosen_rout, 2, "multiChoice") == True:
        if chosen_rout == "1":
            Funktions.inventory_Manager()
            #print player statistics

       # elif chosen_rout == "2":