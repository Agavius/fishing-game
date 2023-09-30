import random, json, time
from dict_data import fish_dict, treasure_dict, trash_dict, level_dict

debug = True
players_json_path = "players.json"


def main():
    global debug, players_json_path

    """
    ___________________________________________________Character loading__________________________________________________________
    """

    if debug == False:
        while True:
            player_name = input("Enter your name: ")
            try:
                player_name = str(player_name).upper()
            except:
                print("Invalid Input")
                continue
            break
    else:
        player_name = "Debug"

    json_file_path = "players.json"
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    variable_to_check = player_name

    try:
        if debug == False:
            value = data[variable_to_check]
            pprint(f"The player '{variable_to_check}' already exists.").black()
            pprint("Now loading player check'.").black()
            time.sleep(1.5)
        else:
            value = data[variable_to_check]
            print("Loaded game in debug mode")
    except KeyError:
        pprint(f"The player '{variable_to_check}' does not exist.").black()
        if debug == False:
            time.sleep(0.5)
        pprint("The player will now be created.").black()
        if debug == False:
            time.sleep(1.2)
        create_new_player(variable_to_check)

    """
    __________________________________________________In Game__________________________________________________________
    """

    while True:
        """
        __________At Home________
        """
        if debug == False:
            pprint(
                "\nYou are at home. What do you want to do?:\n1. Go on a fishing trip.\n2. Go to the market.\n3. Go to bed (Exit the game)"
            ).yellow()
        else:
            print("1. Fishing, 2. Market, 3. Exit")

        if debug == True:
            json_file_path = "players.json"
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)
                print("player data: ", data[player_name])
                # print("removed item: ", remove_from_inventory(player_name))
                # print("player inventory: ", data[player_name]["Possessions"]["Inventory"])

        home_choice = input("\nChoose an option (1/2/3): ")
        """
        __________Home Choices________
        """
        if home_choice == "1":
            print("You are driving to the lake.")
            while True:
                """
                ______At the lake____
                """
                if debug == False:
                    pprint(
                        "\nYou are on a fishing trip\nOptions:\n1. Cast the rod\n2. Go home"
                    ).yellow()
                else:
                    print("\nOptions: 1. Cast the rod, 2. Go home")

                trip_choice = input("\nChoose an option (1/2): ")

                if trip_choice == "1":
                    cast_rod(player_name)
                elif trip_choice == "2":
                    print("You are going back home.")
                    break
                else:
                    print("Invalid choice. Please select 1 or 2.")
        if home_choice == "2":
            """
            ______Shopping____
            """
            go_to_market(player_name)
            time.sleep(2)
            continue
        if home_choice == "3":
            print(f"You are going to bed. See you soon!")
            break
        if home_choice == "clean":
            clean_terminal()
            continue


"""
__________________________________Json Functions_______________________________________________________________
"""


def load_players_data():
    with open(players_json_path, "r") as json_file:
        players_data = json.load(json_file)
    return players_data


def save_new_player(player_name, players_data):
    with open(players_json_path, "w") as json_file:
        new_player = {
            player_name: {
                "Stats": {
                    "Level": 0,
                    "XP": 0,
                    "Strength": 1,
                    "Stamina": 1,
                    "Agility": 1,
                    "Luck": 100,
                },
                "Possessions": {"Moneys": 0, "Inventory": []},
                "Home": {},
                "Highscores": {"Biggest fish:": 0, "Most valuable fish": 0},
            }
        }
        players_data.update(new_player)
        json.dump(players_data, json_file, indent=4)
    return


def dump_json(players_data):
    players_data = players_data
    with open(players_json_path, "w") as json_file:
        json.dump(players_data, json_file, indent=4)
    return


"""
__________________________________Player Functions_______________________________________________________________
"""


def create_new_player(player_name):
    player_name = player_name
    players_data = load_players_data()
    save_new_player(player_name, players_data)
    return


"""
__________________________________Terminal Functions_______________________________________________________________
"""


def clean_terminal():
    print("\033[2J")


class pprint:
    def __init__(self, text):
        self.text = text
        self.text = "m" + self.text + "\033[0m"

    def black(self):
        print(f"\033[30" + self.text)

    def red(self):
        print(f"\033[31" + self.text)

    def green(self):
        print(f"\033[32" + self.text)

    def yellow(self):
        print(f"\033[33" + self.text)

    def blue(self):
        print(f"\033[34" + self.text)

    def magenta(self):
        print(f"\033[35" + self.text)

    def cyan(self):
        print(f"\033[36" + self.text)


class punderline(pprint):
    def __init__(self, text):
        self.text = text
        self.text = ";4m" + self.text + "\033[0m"


"""
__________________________________Fish(ing) Functions_______________________________________________________________
"""
def get_fish_dict_element(element = "weight" or "xp" or "worth"):
    fish_dict_element = []
    if element == "weight":
        for i in range(len(fish_dict)):
            fish_dict_element.append(list(fish_dict.values())[i][0])
        return fish_dict_element
    if element == "xp":
        for i in range(len(fish_dict)):
            fish_dict_element.append(list(fish_dict.values())[i][0])
        return fish_dict_element
    if element == "worth":
        for i in range(len(fish_dict)):
            fish_dict_element.append(list(fish_dict.values())[i][0])
        return fish_dict_element
    
def get_trash_dict_element(element = "weight" or "xp" or "worth"):
    trash_dict_element = []
    if element == "weight":
        for i in range(len(trash_dict)):
            trash_dict_element.append(list(trash_dict.values())[i][0])
        return trash_dict_element
    if element == "xp":
        for i in range(len(trash_dict)):
            trash_dict_element.append(list(trash_dict.values())[i][0])
        return trash_dict_element
    if element == "worth":
        for i in range(len(trash_dict)):
            trash_dict_element.append(list(trash_dict.values())[i][0])
        return trash_dict_element
    
def get_treasure_dict_element(element = "weight" or "xp" or "worth"):
    treasure_dict_element = []
    if element == "weight":
        for i in range(len(treasure_dict)):
            treasure_dict_element.append(list(treasure_dict.values())[i][0])
        return treasure_dict_element
    if element == "xp":
        for i in range(len(treasure_dict)):
            treasure_dict_element.append(list(treasure_dict.values())[i][0])
        return treasure_dict_element
    if element == "worth":
        for i in range(len(treasure_dict)):
            treasure_dict_element.append(list(treasure_dict.values())[i][0])
        return treasure_dict_element
    
def get_fish_worth(item):
    #TODO
    None

def get_fish_xp(item):
    #TODO
    None

def cast_rod(player_name):
    print(f"\n{player_name}, you are now fishing...")
    if debug == False:
        input("Press Enter to cast your line...")
        time_to_catch = random.uniform(0.5, 2.0)
        time.sleep(time_to_catch)
    catch_probability = random.uniform(1.0, 10.0) * float(
        (get_stat(player_name, stat="Luck") / 100)
    )
    if catch_probability > 5.0:
        catch_type = random.choices(["catch_type_fish","catch_type_trash","catch_type_treasure"], weights=[90,8,2])
        if catch_type == "catch_type_fish":
            fish = random.choices(list(fish_dict.keys()), weights=get_fish_dict_element("weight"))
            add_to_inventory(player_name, fish[0])
            if debug == False:
                print(f"\nYou caught a {fish}! Good job, {player_name}!")
            else:
                print(f"You caught a {fish}, catch_probability: {catch_probability}")
        if catch_type == "catch_type_trash":
            trash = random.choices(list(trash_dict.keys()), weights=get_trash_dict_element("weight"))
            add_to_inventory(player_name, trash[0])
            if debug == False:
                print(f"\nYou caught trash. Good job, {player_name} thanks for keeping the ocean clean! You cought {trash} btw.")
            else:
                print(f"You caught trash: {trash}, catch_probability: {catch_probability}")
        if catch_type == "catch_type_treasure":
            treasure = random.choices(list(treasure_dict.keys()), weights=get_treasure_dict_element("weight"))
            add_to_inventory(player_name, treasure[0])
            if debug == False:
                pprint(f"\nYou caught {treasure}, a real treasure! Good job, {player_name}!").magenta()
            else:
                print(f"You caught a {treasure}, catch_probability: {catch_probability}")
        #TODO: Give XP to player
    else:
        if debug == False:
            print("\nOh no, you didn't catch anything this time. Keep trying!")
        else:
            print(
                f"\nYou didn't catch anything, with catch_probability: {catch_probability}"
            )
    return


"""
__________________________________Market Functions_______________________________________________________________
"""


def go_to_market(player_name):
    print(f"The Market is closed for renovations! Come back later.")

    return


"""
__________________________________Inventory Functions_______________________________________________________________
"""


def add_to_inventory(player_name, item):
    player_name = player_name
    players_data = load_players_data()
    inventory = players_data[player_name]["Possessions"]["Inventory"]
    inventory.append(item)
    players_data[player_name]["Possessions"]["Inventory"] = inventory
    dump_json(players_data)
    return


def remove_from_inventory(player_name, item=None):
    if item == None:
        return
    success = False
    player_name = player_name
    players_data = load_players_data()
    inventory = players_data[player_name]["Possessions"]["Inventory"]
    if item in inventory:
        inventory.remove(item)
        players_data[player_name]["Possessions"]["Inventory"] = inventory
        success = True
    dump_json(players_data)
    return success

def get_moneys(player_name):
    player_name = player_name
    players_data = load_players_data()
    moneys = players_data[player_name]["Possessions"]["Moneys"]
    return moneys

def change_moneys(player_name, amount):
    player_name = player_name
    players_data = load_players_data()
    moneys = players_data[player_name]["Possessions"]["Moneys"]
    moneys = moneys + amount
    players_data[player_name]["Possessions"]["Moneys"] = moneys
    dump_json(players_data)
    return


"""
__________________________________Stats Functions_______________________________________________________________
"""


def get_stat(player_name, stat=""):
    if stat == "":
        return
    player_name = player_name
    players_data = load_players_data()
    stat_value = players_data[player_name]["Stats"][stat]
    return stat_value


def change_stat(player_name, stat, change_by: int):
    player_name = player_name
    players_data = load_players_data()
    stat_value = players_data[player_name]["Stats"][stat]
    stat_value = int(stat_value) + change_by
    players_data[player_name]["Stats"][stat] = stat_value
    dump_json(players_data)
    return


def update_level(player_name):
    player_name = player_name
    player_xp = get_stat(player_name, "XP")
    player_level = get_stat(player_name, "Level")
    next_player_level = player_level + 1
    next_player_level_needed_xp = level_dict[next_player_level]
    if player_xp >= next_player_level_needed_xp:
        level_up_player(player_name)
    return


def level_up_player(player_name):
    player_name = player_name
    change_stat(player_name, "Level", change_by=1)
    new_player_level = get_stat(player_name, "Level")
    pprint(
        f"{player_name}, you leveled up! Congratulations. Your new Level is: {new_player_level}."
    ).red()
    pprint("Chose your reward.").red()
    reward_one = random.randint(50, 250)
    reward_two = random.randint(1, 5)
    reward_three = random.choice(["Strength", "Stamina", "Agility"])
    pprint(
        f"(1): {reward_one} Moneys, (2): {reward_two} Luck-Points, (3) Increase {reward_three} by 2."
    ).red()
    reward_choice = input("What do you choose?: ")
    while True:
        if reward_choice == "1":
            change_moneys(player_name, reward_one)
            pprint("Increased Moneys").red()
            break
        if reward_choice == "2":
            change_stat(player_name, "Luck", reward_two)
            pprint("Increased Luck").red()
            break
        if reward_choice == "3":
            change_stat(player_name, reward_three, 2)
            pprint("Increased Stat").red()
            break
    return


"""
__________________________________Option Functions_______________________________________________________________
"""


def options():
    return

"""
__________________________________Main_______________________________________________________________
"""

if __name__ == "__main__":
    clean_terminal()
    pprint(
        r"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~__        __   _                            _          _   _          ~
    ~\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___ ~
    ~ \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \~
    ~  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/~
    ~ __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|~
    ~|  ___(_)___| |__ (_)_ __   __ _   / ___| __ _ _ __ ___   ___| |      ~
    ~| |_  | / __| '_ \| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \ |      ~
    ~|  _| | \__ \ | | | | | | | (_| | | |_| | (_| | | | | | |  __/_|      ~
    ~|_|   |_|___/_| |_|_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___(_)      ~
    ~                           |___/                                      ~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    ).blue()
    while True:
        start_reply = input(
            "Do you want to play (1) or enter the options (2)? (3) or (E) to exit the game.\n"
        )
        if start_reply == "1":
            main()
            break
        if start_reply == "2":
            options()
            clean_terminal()
            continue
        if start_reply == "3" or start_reply == "e" or start_reply == "E":
            print("Thanks for playing! See you Soon.")
            time.sleep(0.25)
            break
