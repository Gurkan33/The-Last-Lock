import random as rand
import json
import simple_colors
import SystemFunktions
import TextOchGubbar
import pathlib
import os
import constants as cons

#------------------------------------------------------#
#Variables

with open(str(pathlib.Path(__file__).parent.resolve())  + "\items.json") as file:
    dict_of_items = json.load(file)

rareties = dict_of_items["dict_rareties"]
items_weapons = dict_of_items["dict_items"]["type"]["weapons"]
enemies = dict_of_items["dict_enemies"]

items_weapons_weight = []
rareties_weight = []
enemies_weight = []

for i in range(0, len(list(items_weapons))):
    items_weapons_weight.append(items_weapons[list(items_weapons)[i]]["weight"])
    
for i in range(0, len(list(rareties))):
    rareties_weight.append(rareties[list(rareties)[i]]["weight"])

for i in range(0, len(list(enemies))):
    enemies_weight.append(enemies[list(enemies)[i]]["weight"])


#------------------------------------------------------#
#Makes item a class

class item_class:
    def __init__(self, item, rarity, dmg):
        self.key = item
        self.item = items_weapons[item]["name"]
        self.rarity = rarity
        self.dmg = dmg
    
    def __str__(self):
        return f"""{eval(rareties[self.rarity]["name_print"])} {simple_colors.black(self.item)} 
dmg: {simple_colors.red(self.dmg)}"""

#------------------------------------------------------#
#Generate item

def generate_item():

    item = list(items_weapons)[rand.randint(0, len(items_weapons)-1)]
    dmg = items_weapons[item]["base_dmg"]
    
    weapon = rand.choices(list(items_weapons), weights=items_weapons_weight, k = 1)[0]
    
    rarity = rand.choices(list(rareties), weights=rareties_weight, k = 1)[0]

    dmg = dmg + rand.randint(rareties[rarity]["dmg_lower"], rareties[rarity]["dmg_upper"])
    
    return item_class(weapon, rareties[rarity]["name"], dmg)

#------------------------------------------------------#  
#Player

class player_class:
    def __init__(self):
        self.name = ""
        self.difficulty = cons.difficulty
        self.equiped = item_class(list(items_weapons)[0], rareties["Special"]["name"], 3)
        self.inventory = []
        self.hp = cons.max_hp
        self.level = 1
        
    def total_dmg(self):
        return int(self.equiped.dmg + cons.base_dmg[self.level-1])
    
    def __str__(self):
        name_print = f"""
Difficulty: {self.difficulty}
Name: {self.name} lvl {self.level}
hp: {self.hp}
Total dmg: {self.total_dmg()}

Equipped item: 
{self.equiped}

Inventory: 
""" + "\n".join(f"{index + 1}.\n{item_class}" for index, item_class in enumerate(self.inventory))
        return name_print

player = player_class()

for i in range(1, 5):
    item = generate_item()
    player.inventory.append(item)

#------------------------------------------------------# 
#Enemy

class enemy_class:
    def __init__(self, enemy_key, enemy_weapon):
        self.key = enemy_key
        self.name = enemies[enemy_key]["name"]
        self.difficulty = cons.difficulty
        self.weapon = enemy_weapon #Kanske en item? Eller custom item?
        self.hp = enemies[enemy_key]["base_hp"]
        self.dmg = ""


    def __str__(self):
        enemy_print =f"""
Difficulty: {self.difficulty}
Name: {self.name}
hp: {self.hp}
weapon: {self.weapon}"""
        return enemy_print
        
#------------------------------------------------------#
#Generate enemy

def generate_enemy():

    enemy_key = list(enemies)[rand.randint(0, len(enemies)-1)]
    
    weapon = generate_item()

    return enemy_class(enemy_key, weapon)


#----------------------------------------------------------------------------#
#Inventory manager
print(generate_enemy())

def player_Manager():

    
    while True:
        os.system('cls')

        print(TextOchGubbar.player_text)
        print(player)
        print("""\n\n What do you want to do?
    [1] Equip an item
    [2] Delet an item
    [3] Nothing""")
        chosen_rout = input(simple_colors.blue("-->",["bold"]))
        
        if SystemFunktions.valid_user_choice(chosen_rout, 3, "multiChoice") == True:


            if chosen_rout == "1": #Equipar ett föremål
                os.system('cls')

                print(TextOchGubbar.inventory)
                print("Witch item do you want to equip?")
                for i in range(0, len(player.inventory)):
                    print(f"{i+1}. \n{player.inventory[i]}")

                print("([Any key] to cancel!)\n")

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(player.inventory), "Your choice isn't in the inventory!") == True:
                    os.system('cls')
                    
                    chosen_item_index = int(chosen_item_index)
                    player.inventory.append(player.equiped)
                    player.equiped =  player.inventory.pop(chosen_item_index-1)
                    print(TextOchGubbar.player_text)
                    print(player)
                    break


            if chosen_rout == "2": #Tar bort en item av spelarens val ifrån inventoryt
                os.system('cls')

                print(TextOchGubbar.inventory)
                print(simple_colors.red("What item do you want to delete? ([Any key] to cancel!)"))
                for i in range(0, len(player.inventory)):
                    print(f"{i+1}. \n{player.inventory[i]}")

                print("([Any key] to cancel!)\n")

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(player.inventory), "Your choice isn't in the inventory!") == True:
                    os.system('cls')

                    chosen_item_index = int(chosen_item_index)

                    print(simple_colors.red("You removed ") + str(player.inventory.pop(chosen_item_index-1)) + simple_colors.red(" from your inventory\n"))
                    
                    for i in range(0, len(player.inventory)):
                        print(f"{i+1}. \n{player.inventory[i]}")
                    break
                        

            if chosen_rout == "3": # Break
                os.system('cls')
                break

#--------------------------------------------------------------------------------#
#Funktion to choos a door

def chooseDoor():
    os.system('cls')

    print(TextOchGubbar.doors)

    print("""Which door do you want to open?
[1] Door 1
[2] Door 2
[3] Door 3
[4] Door 4
          
[5] Go back""")
    
    chosen_rout = input(simple_colors.blue("-->",["bold"]))

    if SystemFunktions.valid_user_choice(chosen_rout, 5, "multiChoice"):
        if chosen_rout == "1":
            door_randomizer()
        elif chosen_rout == "2":
            door_randomizer()
        elif chosen_rout == "3":
            door_randomizer()
        elif chosen_rout == "4":
            ""
            #if player.key == True
        elif chosen_rout == "5":
            ""
            #Exit  

#--------------------------------------------------------------------------------#       
#Funktion för att välja typ av rum

def door_randomizer():
    random_num = rand.randint(1,3)
    if random_num == 1:
        Trap()
    elif random_num == 2:
        Chest()
    elif random_num == 3:
        Encounter()

#--------------------------------------------------------------------------------#
#Funktion for a trap room


def Trap():
    random_Trap = rand.randint(1,30)
    os.system('cls')

    if random_Trap >= 1 and random_Trap <=20:
        print(simple_colors.red(""" Ouch!
        You stepped on nails and lost 10hp!"""))
        player.hp = player.hp-10
        print("\nYour health is now " + simple_colors.red(str(player.hp),["bold"]) + " hp")

    elif random_Trap >= 21 and random_Trap <=29:
        print(simple_colors.red("""Life's tough in prison
        You got in a fight and lost 20hp!"""))
        player.hp = player.hp-20
        print("\nYour health is now " + simple_colors.red(str(player.hp),["bold"]) + " hp")

    elif random_Trap == 30:
        if len(player.inventory) > 0:
            random_invetory_index = rand.randint(1, len(player.inventory)) 
            print(simple_colors.red(f"""Where is my weapon?
You lost your:
{player.equiped.pop(random_invetory_index-1)}
""")) + simple_colors.red("from you inventory to a pickpocket while having lunch!")
        else:
            print(simple_colors.red("A pickpocket tried to steal from you but found nothing"))

    return

#--------------------------------------------------------------------------------#
#Funktion for chest room


def Chest():
    os.system('cls')

    chest_item = generate_item()
    print(F"""You have found a chest containing a:
{chest_item}
Would you like to claim this item?
[1] Yes
[2] No
""")
    while True:
        chosen_input = input(simple_colors.blue("-->",["bold"]))
        if SystemFunktions.valid_user_choice(chosen_input, 2, "multiChoice") == True:
            if chosen_input == "1":

                if len(player.inventory) <= cons.inventory_max_size:
                    player.inventory.append(chest_item)
                    print(f"""{chest_item}
has ben added to your inventory""")
                    break

                elif len(player.inventory) > cons.inventory_max_size:
                    print("""You do not have enough space in your inventory 
would you like to delet an item
[1] Yes
[2] No
""")
                    chosen_input = input(simple_colors.blue("-->",["bold"]))
                    if SystemFunktions.valid_user_choice(chosen_input, 2, "multiChoice") == True:
                        if chosen_input == "1":

                            print(TextOchGubbar.inventory)

                            print(simple_colors.red("What item do you want to delete? ([Any key] to cancel!)"))
                            print(f"""Item from chest:
{chest_item}""")

                            for i in range(0, len(player.inventory)):
                                print(f"{i+1}. \n{player.inventory[i]}")

                            print("([Any key] to cancel!)\n")

                            chosen_item_index = input(simple_colors.blue("-->",["bold"]))

                            if SystemFunktions.valid_user_choice(chosen_item_index, len(player.inventory), "Your choice isn't in the inventory!") == True:
                                chosen_item_index = int(chosen_item_index)

                                print(simple_colors.red("Du tog bort ") + str(player.inventory.pop(chosen_item_index-1)) + simple_colors.red(" från ditt invetory!\n"))
                                
                                print(f"""{chest_item}
has ben added to your inventory
""")
                                player.inventory.append(chest_item)

                                for i in range(0, len(player.inventory)):
                                    print(f"{i+1}. \n{player.inventory[i]}")
                                break

                        elif chosen_input == "2":
                            print(f"""{chest_item}
was left behind
""")
                            break
                        break
                    

            elif chosen_input == "2":
                print(f"""{chest_item}
was left behind
""")
                break 

#--------------------------------------------------------------------------------#
#Funktion for an encounter room

def Encounter():
    os.system('cls')
    
    print(TextOchGubbar.enemy)
    enemy = generate_enemy()

    print(simple_colors.red(f"""Ohh you enountered a {eval(enemies[enemy.key]["name_print"])}
    Take him down and move forward in the prison!"""))

    print(enemy)

    print(TextOchGubbar.VS)

    return

Encounter()

