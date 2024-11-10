import random as rand

items = ["sword", "dager", "knife"]
rareties = ["Common", "Rare", "Epic", "Legendary", "Mythic"]

def item_funk(item, rarity, dmg):
    item_stats = {
      "item": item,
      "rarity": rarity,
      "dmg": dmg
    }
    return item_stats

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
    
    return item_funk(item, rarity, dmg)
    
inventory = []

for i in range(1, 5):
    test = generate_item()
    inventory.append(test)


for i in range(0, len(inventory)):
    print(f"{i+1}. \n {inventory[i]["rarity"]} {inventory[i]["item"]} \n dmg: {inventory[i]["dmg"]}")

