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


print(TextOchGubbar.rubrik)

print(""),
print("")
print(simple_colors.red("Welcome to The Last Lock!",["bold","underlined"]))
print(simple_colors.red("""Your now locked in a prison and have to fight your way out of it!
    Open kests, Fight enemys, Avoid traps and more! """))
print()

player_Name = SystemFunktions.valid_character_name() #Spelare skriver in sitt namn!

print(simple_colors.red("Ohh! Nice name " + simple_colors.blue(str(player_Name)) + "!"))
print("")
print(simple_colors.red("Now " + simple_colors.blue(str(player_Name))) + simple_colors.red(" its time to make your first move!"))