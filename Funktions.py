import random as rand
import json
import simple_colors
import SystemFunktions
import TextOchGubbar
import pathlib
import os
import time
import constants as cons
import ASCII_art as ASCII

#------------------------------------------------------#
#Variables

with open(str(pathlib.Path(__file__).parent.resolve())  + "\items.json") as file:
    dict_of_items = json.load(file)

rareties = dict_of_items["dict_rareties"]
items_weapons = dict_of_items["dict_items"]["type"]["weapons"]
items_consumables = dict_of_items["dict_items"]["type"]["consumable"]
item_types = dict_of_items["dict_items"]["type"]
enemies = dict_of_items["dict_enemies"]

items_weapons_weight = []
items_consumables_weight = []
rareties_weight = []
enemies_weight = []


for i in range(0, len(list(items_consumables))):
    items_consumables_weight.append(items_consumables[list(items_consumables)[i]]["weight"])

for i in range(0, len(list(items_weapons))):
    items_weapons_weight.append(items_weapons[list(items_weapons)[i]]["weight"])
    
for i in range(0, len(list(rareties))):
    rareties_weight.append(rareties[list(rareties)[i]]["weight"])

for i in range(0, len(list(enemies))):
    enemies_weight.append(enemies[list(enemies)[i]]["weight"])


#------------------------------------------------------#
#Makes weapon item a class

class item_weapon_class:
    def __init__(self, item, rarity, dmg):
        self.key = item
        self.name = items_weapons[item]["name"]
        self.rarity = rarity
        self.dmg = dmg
    
    def __str__(self):
        return f"""  {eval(rareties[self.rarity]["name_print"])} {simple_colors.black(self.name)} 
  dmg: {simple_colors.red("+" + str(self.dmg))}"""



#------------------------------------------------------#
#Makes consumable item a class


class item_consumable_class:
    def __init__(self, item) -> None:
        self.key = item
        self.name = items_consumables[item]["name"]
        self.type = items_consumables[item]["type"]
        self.modifier = items_consumables[item]["modifier"]
    def __str__(self):
        if self.type == "hp":
            return f"""  {simple_colors.black(self.name)} 
  +{simple_colors.green(self.modifier)} {simple_colors.green(self.type)}
"""
        elif self.type == "dmg":
            return f"""  {simple_colors.black(self.name)} 
  +{simple_colors.red(self.modifier)} {simple_colors.red(self.type)}
"""
        elif self.type == "speed":
            return f"""{simple_colors.black(self.name)} 
  +{self.modifier} {self.type}
"""
        elif self.type == "accuracy":
            return f"""{simple_colors.black(self.name)} 
  +{self.modifier} {self.type}
"""

#------------------------------------------------------#
#Generate item

def generate_item_consumables():

    consumable = rand.choices(list(items_consumables), weights = items_consumables_weight, k = 1)[0]
    
    return item_consumable_class(consumable)

def generate_item_weapon():

    weapon = rand.choices(list(items_weapons), weights = items_weapons_weight, k = 1)[0]

    dmg = items_weapons[weapon]["base_dmg"]
    
    rarity = rand.choices(list(rareties), weights=rareties_weight, k = 1)[0]

    dmg = dmg + rand.randint(rareties[rarity]["dmg_lower"], rareties[rarity]["dmg_upper"])
    
    return item_weapon_class(weapon, rareties[rarity]["name"], dmg)



def generate_item():
    item_type = rand.choices(["weapons", "consumable"], weights=[1, 1], k = 1)[0]
    if item_type == "weapons":
        item = generate_item_weapon()

    elif item_type == "consumable":
        item = generate_item_consumables()

    return [item, item_type]



#------------------------------------------------------#  
#Player
class player_class:
    def __init__(self):
        self.name = ""
        self.difficulty = cons.difficulty
        self.equiped = item_weapon_class(list(items_weapons)[0], rareties[list(rareties)[-1]]["name"], 3)
        self.inventory_weapons = []
        self.inventory_utilities = []
        self.hp = cons.max_hp
        self.level = 1
        self.speed = cons.player_speed
        self.accuracy = cons.player_accuracy
        self.door_key = False
        
    def total_dmg(self):
        return int(self.equiped.dmg + cons.player_base_dmg_per_level[self.level-1])
    
    def total_inventory_len(self):
        return int(len(self.inventory_weapons) + len(self.inventory_utilities))
    
    def total_inventory(self):
        total_inv = []
        total_inv.append(self.inventory_weapons)
        total_inv.append(self.inventory_utilities)
        return total_inv
    
    def __str__(self):
        name_print = f"""
Name: {self.name} lvl {self.level}
hp: {simple_colors.green(self.hp)}
Total dmg: {simple_colors.red(self.total_dmg())}

Equipped item: 
{self.equiped}

Inventory: 
{"\n".join(f"{index + 1}.\n{item_class}" for index, item_class in enumerate(self.inventory_weapons))}

Utilities:
{"\n".join(f"{index + 1}.\n{item_class}" for index, item_class in enumerate(self.inventory_utilities))}
"""
        return name_print

player = player_class()

for i in range(1, 5):
    item = generate_item_weapon()
    player.inventory_weapons.append(item)

#------------------------------------------------------# 
#Enemy

class enemy_class:
    def __init__(self, enemy_key, enemy_weapon):
        self.key = enemy_key
        self.name = enemies[enemy_key]["name"]
        self.difficulty = cons.difficulty
        self.weapon = enemy_weapon #Kanske en item? Eller custom item?
        self.hp = enemies[enemy_key]["base_hp"]
        self.speed = enemies[enemy_key]["speed"]
        self.accuracy = enemies[enemy_key]["accuracy"]
    
    def total_dmg(self):
        return int(self.weapon.dmg + cons.enemy_base_dmg_per_level[self.level-1])

    def __str__(self):
        enemy_print =f"""
Name: {self.name}
hp: {self.hp}
weapon: {self.weapon}"""
        return enemy_print
        
#------------------------------------------------------#
#Generate enemy

def generate_enemy():

    enemy_key = list(enemies)[rand.randint(0, len(enemies)-1)]
    
    weapon = generate_item_weapon()

    return enemy_class(enemy_key, weapon)


#----------------------------------------------------------------------------#
#Inventory manager

def player_Manager():

    while True:
        os.system('cls')
        print(ASCII.text("PLAYER"))
        print(player)
        print("""\n\n What do you want to do?
    [1] Equip an item
    [2] Delete an item
    [3] Use Utilite
    [4] Nothing""")
        chosen_rout = input(simple_colors.blue("-->",["bold"]))
        
        if SystemFunktions.valid_user_choice(chosen_rout, 4, "multiChoice") == True:


            if chosen_rout == "1": #Equipar ett föremål
                os.system('cls')

                print(ASCII.text("INVENTORY"))
                print(simple_colors.red("Witch item do you want to equip? ([Any key] to cancel!)"))
                for i in range(0, len(player.inventory_weapons)):
                    print(f"{i+1}. \n{player.inventory_weapons[i]}")

                print(simple_colors.red("([Any key] to cancel!)\n"))

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(player.inventory_weapons), "Your choice isn't in the inventory!") == True:
                    os.system('cls')
                    
                    chosen_item_index = int(chosen_item_index)
                    player.inventory_weapons.append(player.equiped)
                    player.equiped =  player.inventory_weapons.pop(chosen_item_index-1)
                    print(ASCII.text("PLAYER"))
                    print(player)
                    break


            elif chosen_rout == "2": #Tar bort en item av spelarens val ifrån inventoryt
                os.system('cls')

                print(ASCII.text("INVENTORY"))
                print(simple_colors.red("What item do you want to delete? ([Any key] to cancel!)"))

                for i in range(0, player.total_inventory_len() - len(player.inventory_utilities)):
                    print(f"{i+1}. \n{player.inventory_weapons[i]}")

                for i in range(0, player.total_inventory_len() - len(player.inventory_weapons)):
                    print(f"{i + 1 + len(player.inventory_weapons)}. \n{player.inventory_utilities[i]}")

                print(simple_colors.red("([Any key] to cancel!)\n"))

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, player.total_inventory_len(), "Your choice isn't in the inventory!") == True:
                    os.system('cls')

                    chosen_item_index = int(chosen_item_index)

                    if chosen_item_index <= len(player.inventory_weapons):
                        print(simple_colors.red("You removed ") + str(player.inventory_weapons.pop(chosen_item_index-1)) + simple_colors.red(" from your inventory\n"))
                    
                    elif chosen_item_index > len(player.inventory_weapons):
                        print(simple_colors.red("You removed ") + str(player.inventory_utilities.pop(chosen_item_index - len(player.inventory_weapons) - 1)) + simple_colors.red(" from your inventory\n"))
                    
                    
                    for i in range(0, len(player.inventory_weapons)):
                        print(f"{i+1}. \n{player.inventory_weapons[i]}")

                    for i in range(0, len(player.inventory_utilities)):
                        print(f"{i + 1 + len(player.inventory_weapons)}. \n{player.inventory_utilities[i]}")

                    break

            elif chosen_rout == "3":
                os.system('cls')

                print(ASCII.text("INVENTORY"))
                print(simple_colors.red("What item do you want to use?"))
                for i in range(0, len(player.inventory_utilities)):
                    print(f"{i+1}. \n{player.inventory_utilities[i]}")

                print(simple_colors.red("([Any key] to cancel!)\n"))

                chosen_item_index = input(simple_colors.blue("-->",["bold"]))
                if SystemFunktions.valid_user_choice(chosen_item_index, len(player.inventory_utilities), "Your choice isn't in the inventory!") == True:
                    os.system('cls')

                    chosen_item_index = int(chosen_item_index)
                    item_used = player.inventory_utilities.pop(chosen_item_index - 1)

                    print(f"You used {item_used}")

                    if item_used.type == "hp":
                        player.hp += item_used.modifier
                        print(f"Player hp is now +{item_used.modifier}")

                    elif item_used.type == "dmg":
                        player.equiped.dmg += item_used.modifier
                        print(f"Player equiped item is now +{item_used.modifier} dmg")

                    elif item_used.type == "speed":
                        player.speed += item_used.modifier
                        print(f"Player speed is now +{item_used.modifier}")

                    elif item_used.type == "accuracy":
                        player.accuracy += item_used.modifier
                        print(f"Player accuracy is now +{item_used.modifier}")
                        
                    
                    break
                        
            elif chosen_rout == "4": # Break
                os.system('cls')
                break

#--------------------------------------------------------------------------------#
#Funktion to choos a door

def chooseDoor():
    os.system('cls')

    print(ASCII.text("DOORS"))

    print(f"""Which door do you want to open?
[1] Door 1
[2] Door 2
[3] Door 3
[4] {simple_colors.blue("Door 4",["italic"])}
          
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
            if player.door_key == True:
                Fourth_door()
            else:
                print(simple_colors.red("\nYou dont have the key\n",["bold"]))
                time.sleep(1)
        elif chosen_rout == "5":
            ""
            #Exit  

#--------------------------------------------------------------------------------#       
#Funktion för att välja typ av rum

def door_randomizer():
    random_num = rand.choices([1, 2, 3], [cons.door_trap, cons.door_chest, cons.door_enemy], k = 1)[0]

    if random_num == 1:
        Trap()
    elif random_num == 2:
        Chest()
    elif random_num == 3:
        Encounter()

#--------------------------------------------------------------------------------#
#Funktion for a trap room


def Trap():
    os.system('cls')
    random_Trap = rand.choices([1, 2, 3], [cons.trap1_weight, cons.trap2_weight, cons.trap3_weight], k = 1)[0]

    if random_Trap == 1:
        print(simple_colors.red(""" Ouch!
        You stepped on nails and lost 10hp!"""))
        player.hp = player.hp-10
        print("\nYour health is now " + simple_colors.red(str(player.hp),["bold"]) + " hp")

    elif random_Trap == 2:
        print(simple_colors.red("""Life's tough in prison
        You got in a fight and lost 20hp!"""))
        player.hp = player.hp-20
        print("\nYour health is now " + simple_colors.red(str(player.hp),["bold"]) + " hp")

    elif random_Trap == 3:
        if player.total_inventory_len() > 0:
            random_invetory_index = rand.randint(0, player.total_inventory_len()-1)
            item_index_lost_by_trap = int()

            if random_invetory_index <= len(player.inventory_weapons):
                item_index_lost_by_trap = random_invetory_index
                item_lost_by_trap = player.inventory_weapons.pop(item_index_lost_by_trap)

            elif random_invetory_index > len(player.inventory_weapons):
                item_index_lost_by_trap = player.total_inventory_len - player.inventory_weapons
                item_lost_by_trap = player.inventory_utilities.pop(item_index_lost_by_trap)

            print(simple_colors.red(f"""Where is my weapon?
You lost your:
{item_lost_by_trap}
""") + simple_colors.red("from you inventory to a pickpocket while having lunch!"))
        else:
            print(simple_colors.red("A pickpocket tried to steal from you but found nothing"))

    return

#--------------------------------------------------------------------------------#
#Funktion for chest room


def Chest():
    os.system('cls')

    chest_item = generate_item()
    chest_item_type = chest_item[1]
    chest_item = chest_item[0]

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

                if player.total_inventory_len() <= cons.inventory_max_size:
                    if chest_item_type == "weapons":
                        player.inventory_weapons.append(chest_item)
                    elif chest_item_type == "consumable":
                        player.inventory_utilities.append(chest_item)
                    
                    print(f"""{chest_item}
has ben added to your inventory""")
                    break

                elif player.total_inventory_len() > cons.inventory_max_size:
                    print("""You do not have enough space in your inventory 
would you like to delet an item
[1] Yes
[2] No
""")
                    chosen_input = input(simple_colors.blue("-->",["bold"]))
                    if SystemFunktions.valid_user_choice(chosen_input, 2, "multiChoice") == True:
                        if chosen_input == "1":

                            print(ASCII.text("INVENTORY"))

                            print(simple_colors.red("What item do you want to delete? ([Any key] to cancel!)"))
                            print(f"""Item from chest:
{chest_item}
""")

                            for i in range(0, player.total_inventory_len()):
                                print(f"{i+1}. \n{player.inventory_weapons[i]}")

                            print("([Any key] to cancel!)\n")

                            chosen_item_index = input(simple_colors.blue("-->",["bold"]))

                            if SystemFunktions.valid_user_choice(chosen_item_index, player.total_inventory_len(), "Your choice isn't in the inventory!") == True:
                                chosen_item_index = int(chosen_item_index)

                                print(simple_colors.red("Du tog bort \n") + str(player.inventory_weapons.pop(chosen_item_index-1)) + simple_colors.red(" från ditt invetory!\n"))
                                
                                print(f"""{chest_item}
has ben added to your inventory
""")
                                if chest_item_type == "weapons":
                                    player.inventory_weapons.append(chest_item)
                                elif chest_item_type == "consumable":
                                    player.inventory_utilities.append(chest_item)

                                print("Weapons")
                                for i in range(0, len(player.inventory_weapons)):
                                    print(f"{i+1}. \n{player.inventory_weapons[i]}")
                                
                                print("Utilites")
                                for i in range(0, len(player.inventory_utilities)):
                                    print(f"{i+1}. \n{player.inventory_utilities[i]}")
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
    
    print(ASCII.text("ENCOUNTER"))
    enemy = generate_enemy()

    print(simple_colors.red(f"""Ohh you enountered a {eval(enemies[enemy.key]["name_print"])}
    """) + simple_colors.red("Take him down to move forward in the prison!"))

    print(enemy)

    print(ASCII.text("vs"))

    print(f"""Name: {player.name}
Equiped: {player.equiped}
Dmg: {player.total_dmg()}
Hp: {player.hp}""")

    while True:
        print("""\nWhat do you wish to do?
[1] Fight
[2] Flee
""")
        
        chosen_input = input(simple_colors.blue("-->",["bold"]))
        if SystemFunktions.valid_user_choice(chosen_input, 2, "multiChoice"):
            if(chosen_input == "2"):
                flee_result = rand.choices([1, 2], [player.speed, enemy.speed], k = 1)[0]

                if flee_result == 1:
                    print(simple_colors.red("You managed to flee! Recover your health and try again later!", ["bold"]))
                    break
                elif flee_result == 2:
                    print(simple_colors.red("You didn't manage to flee, you need to fight your way out of this!", ["bold"]))
            else:
                    
                time.sleep(1)

                dmg_player = player.total_dmg()
                
                hit_result = rand.choices([1, 2], [player.accuracy, enemy.speed], k = 1)[0]
                
                if hit_result == 1:
                    enemy.hp = enemy.hp - dmg_player
                    if enemy.hp <= 0: # Kollar ifall fienden dog
                        print(f"""\nYes! You took down the {eval(enemies[enemy.key]["name_print"])}! And left you at  {simple_colors.green(f"{player.hp}hp",["bold"])}.""")
                        player.level += 1
                        if player.level == 10:
                            player.door_key = True
                            print(simple_colors.red(f"""
Ohh you found a {simple_colors.yellow("key", ["bold"])} !, this might be the key to the {simple_colors.blue("fourth door!",["italic"])}""",["bold"]))
                        break
                    print(f"""You hit the {eval(enemies[enemy.key]["name_print"])} with your {eval(rareties[player.equiped.rarity]["name_print"])} {simple_colors.black(player.equiped.name)}
    and did {simple_colors.red(f"{dmg_player} dmg")}. 
    The enemy hp is now : {simple_colors.green(f"{enemy.hp}hp")}
""")
                else:
                    print(simple_colors.red("You missed your strike!\n",["bold"]))
                        

                time.sleep(1)

                dmg_enemy = enemy.weapon.dmg
                
                hit_result = rand.choices([1, 2], [enemy.accuracy, player.speed], k = 1)[0]

                if hit_result == 1:
                    player.hp = player.hp - dmg_enemy
                    if player.hp <= 0: # Kollar ifall spelaren dog
                        print(simple_colors.red(ASCII.text("Defeat")))
                        print(f"""You died, and lost all your stuff!""")
                        exit() #-------------------------------------------------------------#Dödar programmet!
                    else:
                        print(f"""The {eval(enemies[enemy.key]["name_print"])} hit you with a {eval(rareties[enemy.weapon.rarity]["name_print"])} {simple_colors.black(enemy.weapon.name)}
    and did {simple_colors.red(f"{dmg_enemy} dmg",["bold"])}. 
    Your hp is now : {simple_colors.green(f"{player.hp}hp",["bold"])}
    """)                
                else:
                    print(simple_colors.red(f"The {eval(enemies[enemy.key]["name_print"])} missed his strike!\n",["bold"]))

                

def Fourth_door():

    #----------------------------------- skapar boss enemy
    boss = enemy_class

    boss.hp = cons.boss_hp
    boss.weapon = item_weapon_class(list(items_weapons)[7], rareties[list(rareties)[-2]]["name"], cons.boss_dmg) # ändra bossens startvapen
    boss.speed = cons.boss_speed
    boss.accuracy = cons.boss_accuracy
    boss.name = cons.boss_name
    #-----------------------------------




    print(simple_colors.blue(ASCII.text("DOOR 4")))
    print(simple_colors.red(f"""You have entered the {simple_colors.blue("fourth door",["italic"])} {simple_colors.red("""!
    Here you will face the last obstacle before escaping the prison!""")}
                            
                            """))
    i = True
    while i == True: #En sista chas att kolla inventoryt
        print(f"""\nChose what you wish to do!
        [1] Look at player info
        [2] {simple_colors.red("Take on the fight",["bold"])}""")

        
        chosen_rout = input(simple_colors.blue("-->",["bold"]))
        if SystemFunktions.valid_user_choice(chosen_rout, 2, "multiChoice") == True:
            if chosen_rout == "1":
                player_Manager()
                

            elif chosen_rout == "2":
                i = False
    
    while True:
        time.sleep(1)

        dmg_player = player.total_dmg()
                    
        hit_result = rand.choices([1, 2], [player.accuracy, boss.speed], k = 1)[0]
                    
        if hit_result == 1:
            boss.hp = boss.hp - dmg_player
            if boss.hp <= 0: #------------------------------------YOU WIN THE GAME!----------------------------------------
                print(f"""Yes! You took down the {simple_colors.red(boss.name)}! And left you at  {simple_colors.green(f"{player.hp}hp",["bold"])}.
                      now your on free foot!""")
                
                print(TextOchGubbar.player_walk)
            
                exit() #-------------------------------------------------------------#Dödar programmet!----------------------------------
            else:
                print(f"""You hit the {simple_colors.red(boss.name)} with your {eval(rareties[player.equiped.rarity]["name_print"])} {simple_colors.black(player.equiped.name)}
    and did {simple_colors.red(f"{dmg_player} dmg")}. 
    The enemy hp is now : {simple_colors.green(f"{boss.hp}hp")}
        """)
        else:
            print(simple_colors.red("You missed your strike!\n",["bold"]))
                        

        time.sleep(1)

        dmg_enemy = boss.weapon.dmg
                    
        hit_result = rand.choices([1, 2], [boss.accuracy, player.speed], k = 1)[0]

        if hit_result == 1:
            player.hp = player.hp - dmg_enemy
            if player.hp <= 0:
                print(simple_colors.red(ASCII.text("Defeat")))
                print(f"""You died, and lost all your stuff!""")
                exit() #-------------------------------------------------------------#Dödar programmet!
            else:
                print(f"""The {simple_colors.red(boss.name)} hit you with a {eval(rareties[boss.weapon.rarity]["name_print"])} {simple_colors.black(boss.weapon.name)}
    and did {simple_colors.red(f"{dmg_enemy} dmg",["bold"])}. 
    Your hp is now : {simple_colors.green(f"{player.hp}hp",["bold"])}
        """)                
        else:
            print(simple_colors.red(f"The Enemy missed his strike!\n",["bold"]))

        
#F

# Trap()

# Encounter()

# print(generate_enemy())

# player.inventory_utilities.append(generate_item)

# print(player.total_inventory_len())