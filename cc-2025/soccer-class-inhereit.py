class Person:
    def __init__(self, name,
                 age,
                 address):
        self.name = name
        self.age = age
        self.address = address

    def print_person(self):
        print(f"{self.name} - Age {self.age}")
        print(f"{self.name} - Address {self.address}")


class Manager(Person):
    def __init__(self, name,
                 age,
                 address,
                 team):
        super().__init__(name, age, address)
        self.team = team


class Coach(Person):
    def __init__(self,
                 name,
                 age,
                 address,
                 manager,
                 manager_type):
        super().__init__(name, age, address)
        self.manager = manager
        self.manager_type = manager_type


class Player(Person):
    def __init__(self, name,
                 age,
                 address,
                 goals,
                 teams,
                 games,
                 position):
        super().__init__(name, age, address)
        self.goals = goals
        self.teams = teams
        self.games = games
        self.position = position

    def print_player(self):
        self.print_person()
        print(f"{self.name} - Number of goals {self.goals}")
        print(f"{self.name} - Number of games {self.games}")
        print(f"{self.name} - Teams {self.teams}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    messi = Player('Messi', 200, '123 main st', ['Miami'], 35, 100, 'Right Wing')
    ronaldo = Player('Ronaldo', 220, '456 state st', ['Al Nasr'], 40, 150, 'Striker')

    messi.print_player()
    ronaldo.print_player()
