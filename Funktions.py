import random as rand
import json
import simple_colors
import SystemFunktions

#------------------------------------------------------#

with open("items.json") as file:
    dict_of_items = json.load(file)

rareties = ["Common", "Rare", "Epic", "Legendary", "Mythic"]
items_keys = list(dict_of_items.keys())
items = []
inventory =[]

for i in range(0, len(list(dict_of_items.keys()))):
    items.append(dict_of_items[items_keys[i]]["name"])

class item_class:
    def __init__(self, item, rarity, dmg):
        self.item = item
        self.rarity = rarity
        self.dmg = dmg
    
    def __str__(self):
        return f"{self.rarity} {self.item} dmg: {self.dmg}"


def generate_item():

    item = items[rand.randint(0, len(items)-1)]
    rarity = rareties[rand.randint(0, len(rareties)-1)]
    dmg = 0

    if rarity == "Common":
        dmg = dmg + rand.randint(1, 5)

    elif rarity == "Rare":
        dmg = dmg + rand.randint(3, 7)

    elif rarity == "Epic":
        dmg = dmg + rand.randint(5, 9)

    elif rarity == "Legendary":
        dmg = dmg + rand.randint(7, 11)
    
    elif rarity == "Mythic":
        dmg = dmg + rand.randint(9, 13)
    
    return item_class(item, rarity, dmg)

for i in range(1, 5):
    item = generate_item()
    inventory.append(item)
    

#------------------------------------------------------#

def inventory_Manager():
    for i in range(0, len(inventory)):
        print(f"{i+1}. \n {inventory[i]}")
    
    while True:
        print("""\n\nWhat do you want to do?
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
                    print(f"{i+1}. \n {inventory[i]}")

                print("([Any key] to cancel!)\n")

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(inventory), "Your choice isn't in the inventory!"):

                    print(simple_colors.red("Du tog bort ") + simple_colors.magenta(str(inventory[i]),["italic"]) + simple_colors.red(" från ditt invetory!\n"))
                    del inventory[int(chosen_item_index)-1]
                    
                    for i in range(0, len(inventory)):
                        print(f"{i+1}. \n {inventory[i]}")
                        

            if chosen_rout == "3": # Break
                break
        
    

