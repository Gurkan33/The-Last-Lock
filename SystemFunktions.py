import simple_colors

def valid_character_name(): # Kolla valida namn
    while True:  
        name = input(simple_colors.blue("Chose a name for you character: ",["bold"])) 

        # Kollar om namnet bara innehåller bokstäver
        if len(name)>=3:
            return name  # Returnerar det giltiga namnet
        else:
            print(simple_colors.red("Wrong name! Your name must be longer than 3 characters!",["bold","underlined"]))


def valid_user_choice(choice, option_amount):
    while True:
        try:
            choice = int(choice)
            len_of_list = list(range(1, option_amount+1))
            if choice in len_of_list:
                return True
            else:
                print(simple_colors.red("Invalid input. Your choice ") + simple_colors.blue(str(choice)) + simple_colors.red(" isn't in ")  + simple_colors.blue(str(len_of_list)))
                return False

        except ValueError:
            print(simple_colors.red("Invalid input, your choce must be a number!. Your choice : ") + simple_colors.blue(str(choice)))
            return False
        

        