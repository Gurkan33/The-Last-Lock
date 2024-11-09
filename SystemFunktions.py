import simple_colors

def valid_character_name(): # Kolla valida namn
    while True:  
        name = input(simple_colors.blue("Chose a name for you character: ",["bold"])) 

        # Kollar om namnet bara innehåller bokstäver
        if name.isalpha():
            return name  # Returnerar det giltiga namnet
        else:
            print(simple_colors.red("Felaktigt namn! Använd endast bokstäver. Försök igen!",["bold","underlined"]))