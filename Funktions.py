import random as rand
import json
import simple_colors
import SystemFunktions
import TextOchGubbar
import pathlib

#------------------------------------------------------#
#Variables

with open(str(pathlib.Path(__file__).parent.resolve())  + "\items.json") as file:
    dict_of_items = json.load(file)

rareties = dict_of_items["dict_rareties"]
items = dict_of_items["dict_items"]["type"]["weapons"]
name = ""
inventory_max_size = 3

#------------------------------------------------------#
#Makes item a class

class item_class:
    def __init__(self, item, rarity, dmg):
        self.item = item
        self.rarity = rarity
        self.dmg = dmg
    
    def __str__(self):
        return f"{eval(rareties[self.rarity]["name_print"])} {simple_colors.black(self.item)} \n  dmg: {simple_colors.red(self.dmg)}"

#------------------------------------------------------#
#Generate item

def generate_item():

    item = list(items)[rand.randint(0, len(items)-1)]
    rarity = rareties[list(rareties)[rand.randint(0, len(list(rareties))-2)]]["name"]
    dmg = items[item]["base_dmg"]

    if rarity == rareties["Common"]["name"]:
        dmg = dmg + rand.randint(1, 5)

    elif rarity == rareties["Rare"]["name"]:
        dmg = dmg + rand.randint(3, 7)

    elif rarity == rareties["Epic"]["name"]:
        dmg = dmg + rand.randint(5, 9)

    elif rarity == rareties["Legendary"]["name"]:
        dmg = dmg + rand.randint(7, 11)
    
    elif rarity == rareties["Mythic"]["name"]:
        dmg = dmg + rand.randint(9, 13)
    
    return item_class(item, rarity, dmg)
 


#------------------------------------------------------#  
#Player

class player_class:
    def __init__(self):
        self.name = ""
        self.difficulty = int(1)
        self.equiped = item_class(items["Stick"]["name"], rareties["Special"]["name"], 10)
        self.inventory = []
        self.hp = 100
        self.level = 1
    def __str__(self):
        name_print = f"""
Name: 
{self.name} lvl {self.level}
hp: {self.hp}

Difficulty: {self.difficulty}

Equipped item: 
{self.equiped}

Inventory: 
""" + "\n".join(f"{index + 1}.\n{item_class}" for index, item_class in enumerate(self.inventory))
        return name_print

player = player_class()

for i in range(1, 5):
    item = generate_item()
    player.inventory.append(item)

#----------------------------------------------------------------------------#
#Inventory manager

def player_Manager():

    
    while True:
        print(TextOchGubbar.player_text)
        print(player)
        print("""\n\n What do you want to do?
    [1] Equip an item
    [2] Delet an item
    [3] Nothing""")
        chosen_rout = input(simple_colors.blue("-->",["bold"]))
        
        if SystemFunktions.valid_user_choice(chosen_rout, 3, "multiChoice") == True:


            if chosen_rout == "1": #Equipar ett föremål
                print(TextOchGubbar.inventory)
                print("Witch item do you want to equip?")
                for i in range(0, len(player.inventory)):
                    print(f"{i+1}. \n{player.inventory[i]}")

                print("([Any key] to cancel!)\n")

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(player.inventory), "Your choice isn't in the inventory!") == True:
                    chosen_item_index = int(chosen_item_index)
                    player.inventory.append(player.equiped)
                    player.equiped =  player.inventory.pop(chosen_item_index-1)
                    print(TextOchGubbar.player_text)
                    print(player)
                    break


            if chosen_rout == "2": #Tar bort en item av spelarens val ifrån inventoryt
                print(TextOchGubbar.inventory)
                print(simple_colors.red("What item do you want to delete? ([Any key] to cancel!)"))
                for i in range(0, len(player.inventory)):
                    print(f"{i+1}. \n{player.inventory[i]}")

                print("([Any key] to cancel!)\n")

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(player.inventory), "Your choice isn't in the inventory!") == True:
                    chosen_item_index = int(chosen_item_index)

                    print(simple_colors.red("Du tog bort ") + str(player.inventory.pop(chosen_item_index-1)) + simple_colors.red(" från ditt invetory!\n"))
                    
                    for i in range(0, len(player.inventory)):
                        print(f"{i+1}. \n{player.inventory[i]}")
                    break
                        

            if chosen_rout == "3": # Break
                break

#--------------------------------------------------------------------------------#

def chooseDoor():
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
                   

def door_randomizer():
    random_num = rand.randint(1,3)
    if random_num == 1:
        Trap()
    elif random_num == 2:
        Chest()
    elif random_num == 3:
        Encounter()

def Trap():
    print("trap")
    return
    #Trap

def Chest():
    chest_item = generate_item()
    print(F"""You have found a chest with a:
{chest_item}
Would you like to claim this item?
[1] Yes
[2] No
""")
    while True:
        chosen_input = input(simple_colors.blue("-->",["bold"]))
        if SystemFunktions.valid_user_choice(chosen_input, 2, "multiChoice") == True:
            if chosen_input == "1":

                if len(player.inventory) <= inventory_max_size:
                    player.inventory.append(chest_item)
                    print(f"""{chest_item}
has ben added to your inventory""")
                    break

                elif len(player.inventory) > inventory_max_size:
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
    #Chest

def Encounter():
    print("Encounter")
    return
    #Encounter





