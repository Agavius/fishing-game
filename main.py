import random
import json
import time

debug = False
players_json_path = "players.json"


def main():
    global debug, players_json_path
    print("Welcome to the Fishing Game!")

    """
    ______________________________________________________________________________________________________________________
    """

    if debug == False:
        while True:
            player_name = input("Enter your name: ")
            try:
                if player_name == "Debug":
                    print(f"Debug Mode is now on")
                    debug = True
                    break
                player_name = str(player_name).upper()
            except:
                print(f"Invalid Input")
                continue
            break
    else:
        player_name = "Debug"

    json_file_path = 'players.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    variable_to_check = player_name

    try:
        if debug == False:
            value = data[variable_to_check]
            print(f"The player '{variable_to_check}' already exists.")
            print(f"Now loading player '{variable_to_check}'.")
            time.sleep(1.5)
        else:
            print(f"Loaded game in debug mode")
    except KeyError:
        print(f"The player '{variable_to_check}' does not exist.")
        if debug == False:
            time.sleep(0.5)
        print(f"The player '{variable_to_check}' will now be created.")
        if debug == False:
            time.sleep(1.2)
        create_new_player(variable_to_check)

    """
    ______________________________________________________________________________________________________________________
    """

    while True:
        if debug == False:
            print("\nYou are at home. What do you want to do?:")
            print("1. Go on a fishing trip.")
            print("2. Go shopping.")
            print("3. Go to bed (Exit the game).")
        else:
            print("1. Fishing, 2. Shoppping, 3. exit")

        if debug == True:
            json_file_path = 'players.json'
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                print("player data: ", data[player_name])
                # print("removed item: ", remove_from_inventory(player_name))
                # print("player inventory: ", data[player_name]["Possessions"]["Inventory"])

        home_choice = input("\nChoose an option (1/2/3): ")
        if home_choice == "1":
            while True:
                if debug == False:
                    print("\nYou are on a fishing trip\nOptions:")
                    print("1. Cast the rod")
                    print("2. Go home")
                else:
                    print("\nOptions: 1. Cast the rod, 2. Go home")

                trip_choice = input("\nChoose an option (1/2): ")

                if trip_choice == "1":
                    go_fishing(player_name)
                elif trip_choice == "2":
                    print("You are going back home.")
                    break
                else:
                    print("Invalid choice. Please select 1 or 2.")
        if home_choice == "2":
            go_shopping(player_name)
            time.sleep(2)
            continue
        if home_choice == "3":
            print(f"You are going to bed. See you soon!")
            break


"""
__________________________________Json Functions_______________________________________________________________
"""


def load_players_data():
    with open(players_json_path, 'r') as json_file:
        players_data = json.load(json_file)
    return players_data


def save_new_player(player_name, players_data):
    with open(players_json_path, 'w') as json_file:
        new_player = {player_name:
                      {
                          "Stats": {"Level": 0, "XP": 0, "Strength": 1, "Stamina": 1, "Luck": 100},
                          "Possessions": {"Moneys": 0, "Inventory": []},
                          "Home": {},
                          "Highscores": {"Biggest fish:": 0, "Most valuable fish": 0}
                      }
                      }
        players_data.update(new_player)
        json.dump(players_data, json_file, indent=4)
    return


def dump_json(players_data):
    players_data = players_data
    with open(players_json_path, 'w') as json_file:
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
__________________________________Choices Functions_______________________________________________________________
"""


def go_fishing(player_name):
    print(f"\n{player_name}, you are now fishing...")

    if debug == False:
        input("Press Enter to cast your line...")
        time_to_catch = random.uniform(0.5, 2.0)
        time.sleep(time_to_catch)

    catch_probability = (random.uniform(1.0, 10.0) *
                         float((get_stat(player_name, stat="Luck") / 100)))

    if catch_probability > 5.0:
        fish = random.choice(["bass", "trout", "catfish"])
        add_to_inventory(player_name, fish)
        if debug == False:
            print(f"\nYou caught a {fish}! Good job, {player_name}!")
        else:
            print(
                f"You caught a {fish}, catch_probability: {catch_probability}")

    else:
        if debug == False:
            print("\nOh no, you didn't catch anything this time. Keep trying!")
        else:
            print(
                f"\nYou didn't catch anything, with catch_probability: {catch_probability}")

    return


def go_shopping(player_name):
    print(f"The Market is closed for renovations! Come back later")

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


if __name__ == "__main__":
    main()
