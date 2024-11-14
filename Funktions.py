import random as rand
import json
import simple_colors
import SystemFunktions
import TextOchGubbar

#------------------------------------------------------#
#Variables

with open("items.json") as file:
    dict_of_items = json.load(file)
rareties_print = {
    "Common": simple_colors.black("Common"), 
    "Rare": simple_colors.blue("Rare"), 
    "Epic": simple_colors.magenta("Epic"), 
    "Legendary": simple_colors.yellow("Legendary"), 
    "Mythic": simple_colors.red("Mythic",["italic","bright"]),
    "Special": "Special"
    }
rareties = dict_of_items["dict_rareties"]
items = dict_of_items["dict_items"]
name = ""


#------------------------------------------------------#
#Makes item a class

class item_class:
    def __init__(self, item, rarity, dmg):
        self.item = item
        self.rarity = rarity
        self.dmg = dmg
    
    def __str__(self):
        return f"{rareties_print[self.rarity]} {simple_colors.black(self.item)} \n  dmg: {simple_colors.red(self.dmg)}"

#------------------------------------------------------#
#Generate item

def generate_item():

    item = list(items)[rand.randint(0, len(items)-1)]
    rarity = list(rareties)[rand.randint(0, len(list(rareties))-1)]
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
#Start of game
def start_of_game():
    print(TextOchGubbar.rubrik + "\n\n")

    print(simple_colors.red("Welcome to The Last Lock!",["bold","underlined"]))
    print(simple_colors.red("""Your now locked in a prison and have to fight your way out of it!
        Open kests, Fight enemys, Avoid traps and more! \n"""))
    
    player_Name = SystemFunktions.valid_character_name() #Spelare skriver in sitt namn!
    player.name = player_Name

    print(simple_colors.red("Ohh! Nice name " + simple_colors.blue(str(player_Name)) + "!\n"))

    print(simple_colors.red("Now ") + simple_colors.blue(str(player_Name)) + simple_colors.red(" its time to make your first move!"))

    print(simple_colors.red("""What do you want to do?."""))


#------------------------------------------------------#  
#Player

class player_class:
    def __init__(self):
        self.name = ""
        self.difficulty = int(1)
        self.equiped = item_class(items["Stick"]["name"], "Special", 10)
        self.inventory = []
        self.level = 1
    def __str__(self):
        name_print = f"""
Name: {self.name} lvl {self.level}
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

#------------------------------------------------------#
#Inventory manager

def inventory_Manager():

    
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
                    player.equiped = player.inventory[chosen_item_index-1]
                    print(TextOchGubbar.player_text)
                    print(player)
                    break


            if chosen_rout == "2": #Tar bort en item av spelarens val ifrån inventoryt
                print(simple_colors.red("What item do you want to delete? ([Any key] to cancel!)"))
                print(TextOchGubbar.inventory)
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