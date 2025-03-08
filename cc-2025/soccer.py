# This is a sample Python script.

# Press ⌃R t `
def print_hi(name):
    print(f'Hi, {name}')


soccer_players = {
    "Neymar": {
        "Number of Goals": 5,
        "Teams": ["Brazil", "Barcelona", "PSG"],
        "Age": 33,
        "Number of Games": 20,
        "Position": "Left Wing"
    },
    "Messi": {
        "Number of Goals": 6,
        "Teams": ["Argentina", "Barcelona", "PSG"],
        "Age": 37,
        "Number of Games": 25,
        "Position": "Right Wing"
    },
    "Ronaldo": {
        "Number of Goals": 5,
        "Teams": ["Portugal", "Real Madrid", "Al Nasr"],
        "Age": 40,
        "Number of Games": 29,
        "Position": "Striker"
    },
    "Kane": {
        "Number of Goals": 3,
        "Teams": ["England", "Tottenham"],
        "Age": 40,
        "Number of Games": 29,
        "Position": "Striker"
    },
}

def find_position(position):
    for name in soccer_players.keys():
        player = soccer_players[name]
        if player["Position"] == position:
            print(f"Player: {name} - Player Info : {player}")


def print_player(name):
    print(f"{name} - Number of goals {soccer_players[name]['Number of Goals']}")
    print(f"{name} - Age {soccer_players[name]['Age']}")
    print(f"{name} - Number of games {soccer_players[name]['Number of Games']}")
    print(f"{name} - Teams {soccer_players[name]['Teams']}")


def add3(x, y, z):
    return x + y + z


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = 5
    y = 7
    # print(f"{add(x, y)}")
    # print_player("Messi")
    # print_player("Neymar")
    # print_player("Ronaldo")
    # print_player("Kane")
    # find_position("Right Wing")

    # list_of_numbers = [1, 6, 3, 8, 9]
    #
    # for thingy in list_of_numbers:
    #     if thingy % 2 == 1:
    #         print(thingy)

    for first_number in range(1, 13):
        for second_number in range(1, 13):
            print(first_number * second_number)

