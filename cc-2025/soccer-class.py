# This is a sample Python script.

# Press ⌃R t `
def print_hi(name):
    print(f'Hi, {name}')

class Player:
    def __init__(self, name,
                 goals,
                 teams,
                 age,
                 games,
                 position):
        self.name = name
        self.goals = goals
        self.teams = teams
        self.age = age
        self.games = games
        self.position = position

    def print_player(self):
        print(f"{self.name} - Number of goals {self.goals}")
        print(f"{self.name} - Age {self.age}")
        print(f"{self.name} - Number of games {self.games}")
        print(f"{self.name} - Teams {self.teams}")


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

    # print_player("Messi")
    # print_player("Neymar")
    # print_player("Ronaldo")
    # print_player("Kane")
    # find_position("Right Wing")
    messi = Player('Messi', 200, ['Miami'], 35, 100, 'Right Wing')
    ronaldo = Player('Ronaldo', 220, ['Al Nasr'], 40, 150, 'Striker')

    messi.print_player()
    ronaldo.print_player()

    ronaldo.