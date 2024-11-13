import random as rand
import json
import simple_colors
import SystemFunktions

#------------------------------------------------------#
#Variables

with open("items.json") as file:
    dict_of_items = json.load(file)

rareties = [simple_colors.black("Common"), simple_colors.blue("Rare"), simple_colors.magenta("Epic"), simple_colors.yellow("Legendary"), simple_colors.red("Mythic",["italic","bright"])]
items_keys = list(dict_of_items.keys())
items = []
inventory =[]
name = ""
difficulty = int(1)

for i in range(0, len(list(dict_of_items.keys()))):
    items.append(dict_of_items[items_keys[i]]["name"])

#------------------------------------------------------#
#Makes item a class

class item_class:
    def __init__(self, item, rarity, dmg):
        self.item = item
        self.rarity = rarity
        self.dmg = dmg
    
    def __str__(self):
        return f"{self.rarity} {simple_colors.black(self.item)} \n  dmg: {simple_colors.red(self.dmg)}"

#------------------------------------------------------#
#Generate item

def generate_item():

    item = items[rand.randint(0, len(items)-1)]
    rarity = rareties[rand.randint(0, len(rareties)-1)]
    dmg = int()

    if rarity == rareties[0]:       #Common
        dmg = dmg + rand.randint(1, 5)

    elif rarity == rareties[1]:     #Rare
        dmg = dmg + rand.randint(3, 7)

    elif rarity == rareties[2]:     #Epic
        dmg = dmg + rand.randint(5, 9)

    elif rarity == rareties[3]:     #Legendary
        dmg = dmg + rand.randint(7, 11)
    
    elif rarity == rareties[4]:     #Mythic
        dmg = dmg + rand.randint(9, 13)
    
    return item_class(item, rarity, dmg)

for i in range(1, 5):
    item = generate_item()
    inventory.append(item)

#------------------------------------------------------#  
#Starter weapon

starter_weapon = item_class(0, 0, 0)
starter_weapon.item = items[0]
starter_weapon.rarity = "Special"
starter_weapon.dmg = 10

#------------------------------------------------------#
#Player

class player:
    def __init__(self):
        self.name = name
        self.difficulty = difficulty
        self.equiped = starter_weapon
        self.player_inventory = inventory
    def __str__(self):
        name_print = f"""
Name: {self.name} 
Difficulty: {self.difficulty}

Equipped item: 
{self.equiped}

Inventory: 
""" + "\n".join(f"{index + 1}.\n{item_class}" for index, item_class in enumerate(inventory))
        
        return name_print

print(player())

#------------------------------------------------------#
#Inventory manager

def inventory_Manager():
    for i in range(0, len(inventory)):
        print(f"{i+1}. \n{inventory[i]}")
    
    while True:
        print("""\n\n What do you want to do?
    [1] Equip an item
    [2] Delet an item
    [3] Nothing""")
        chosen_rout  = input(simple_colors.blue("-->",["bold"]))
        
        if SystemFunktions.valid_user_choice(chosen_rout, 3, "multiChoice") == True:


            if chosen_rout == "1": #Equipar ett föremål
                print("1")



            if chosen_rout == "2": #Tar bort en item av spelarens val ifrån inventoryt
                print(simple_colors.red("What item do you want to delete? ([Any key] to cancel!)"))
                for i in range(0, len(inventory)):
                    print(f"{i+1}. \n{inventory[i]}")

                print("([Any key] to cancel!)\n")

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(inventory), "Your choice isn't in the inventory!"):
                    chosen_item_index = int(chosen_item_index)

                    print(simple_colors.red("Du tog bort ") + str(inventory.pop(chosen_item_index-1)) + simple_colors.red(" från ditt invetory!\n"))
                    
                    for i in range(0, len(inventory)):
                        print(f"{i+1}. \n{inventory[i]}")
                        

            if chosen_rout == "3": # Break
                break