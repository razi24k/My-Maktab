import random
from itertools import permutations


class Human:
    def __init__(self, name, age):
        self.name = name
        assert isinstance(age, int) and age >= 0, "Age must be a positive integer"
        self.age = age


class Player(Human):
    def __init__(self, name, age, right, post, score):
        assert isinstance(age, (int, float)) and 15 <= age <= 30, "Age is out of range"
        super().__init__(name, age)
        assert isinstance(right, (float, int)) and right > 0, "Right must be a positive float or integer"
        self.right = right
        self.post = post
        assert isinstance(score, (int, float)) and 0 <= score <= 100, "Score is out of range"
        self.score = score


class Coach(Human):
    def __init__(self, name, age, right, start_contract, end_contract, is_busy=False):
        assert 30 <= age <= 65, "Age is out of range"
        super().__init__(name, age)
        assert isinstance(right, (float, int)) and right > 0, "Right must be a positive float or integer"
        self.right = right
        self.start_contract = start_contract
        self.end_contract = end_contract
        self.is_busy = is_busy

    def add_to_team(self):
        if not self.is_busy:
            self.is_busy = True
        else:
            print("This coach is already busy in another team...")


class Team:
    teams = []

    def __init__(self, name, point, coach, balance=0):
        self.name = name
        assert isinstance(point, int) and 0 <= point, "Point must be a positive integer"
        self.point = point
        assert isinstance(coach, Coach), "Coach must be an object of type Coach"
        self.coach = coach
        self.players = []
        assert len(self.players) <= 11, (self.players.pop(), "The team is full...")
        assert isinstance(balance, (int, float)) and 0 <= balance
        self.balance = balance
        Team.teams.append(self)

    def add_player(self, name):
        assert isinstance(name, Player), "Player must be an object of type Player"
        self.players.append(name)

    def get_player(self, name, amount):
        self.balance -= amount
        self.players.append(name)

    def give_player(self, name, amount):
        player = self.players.pop(self.players.index(name))
        self.balance += amount
        return player

    def apply_points(self, result):
        if result == "win":
            self.point += 3
        elif result == "draw":
            self.point += 1
        else:
            self.point = self.point


class League:
    @staticmethod
    def play_matches():
        the_league_map = permutations(Team.teams, 2)
        for game in the_league_map:
            team_1_win = random.choice(["win", "draw", "lose"])
            game[0].apply_points(team_1_win)
            if team_1_win == "win":
                game[1].apply_points("lose")
            elif team_1_win == "draw":
                game[1].apply_points("draw")
            else:
                game[1].apply_points("win")

    @staticmethod
    def draw():
        Team.teams.sort(key=lambda self: self.point, reverse=True)
        print("_" * 89)
        print("|", "Team".center(16), "|", "Points".center(10), "|")
        print("_" * 89)
        for i in Team.teams:
            print("|", i.name.center(16), "|", str(i.point).center(10), "|")
            print("_" * 89)

# team1 = Team("Esteghlal", 16)
# print(team1.validate_coach("Nekoonam"))
# print(Team.teams_list[0].coach)
