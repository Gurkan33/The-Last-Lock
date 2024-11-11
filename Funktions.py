import random as rand
import json
import simple_colors

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
    print("""
What do you want to do?
    [1] Equip an item
    [2] Delet an item
    [3] Nothing""")

    

