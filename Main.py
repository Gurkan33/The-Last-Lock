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

import TextOchGubbar
import simple_colors 

print(TextOchGubbar.rubrik)

print("===================================================================")
print(simple_colors.red("Welcome to The Last Lock!",["bold","underlined"]))
print("Your now locked in a prison and have to fight your way out of it!")
print("")
player_Name = input