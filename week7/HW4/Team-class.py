import random
from itertools import permutations
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Team:
    teams = []

    def __init__(self, name, points=0, game_num=0, win_num=0, draw_num=0, lose_num=0):
        self.name = name
        self.points = points
        self.game_num = int(game_num)
        self.win_num = int(win_num)
        self.draw_num = int(draw_num)
        self.lose_num = int(lose_num)
        Team.teams.append(self)

    def apply_points(self, result):
        if result == "win":
            self.points += 3
            self.win_num += 1
        elif result == "draw":
            self.points += 1
            self.draw_num += 1
        else:
            self.lose_num += 1
        self.game_num += 1

    @classmethod
    def add_team(cls, the_team):
        cls(the_team)

    @staticmethod
    def main_menu():
        print(f'''{"Main Menu".center(42, "*")}
*{"1. Show League Table".center(40)}*
*{"2. Enter Teams".center(40)}*
*{"3. Exit".center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice

    @classmethod
    def draw(cls):
        cls.teams.sort(key=lambda self: self.points, reverse=True)
        print("_" * 89)
        print("|", "Team".center(16), "|", "Points".center(10), "|", "Matches Played".center(15), "|",
              "Wins".center(10), "|", "Draws".center(10), "|", "Loses".center(10), "|")
        print("_" * 89)
        for i in cls.teams:
            print("|", i.name.center(16), "|", str(i.points).center(10), "|", str(i.game_num).center(15),
                  "|", str(i.win_num).center(10), "|", str(i.draw_num).center(10), "|", str(i.lose_num).center(10), "|")
            print("_" * 89)


print("Welcome to my amazing league! ")
input("Press Enter to continue...")
exit_program = False
while not exit_program:
    # clear()
    my_menu = Team.main_menu()
    if my_menu == "1":
        clear()
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
        Team.draw()
    elif my_menu == "2":
        Team.teams.clear()
        clear()
        while True:
            team = input("Enter Team name(enter Exit to back to menu): ")
            if team.lower() == "exit":
                break
            else:
                Team.add_team(team)
    elif my_menu == "3":
        clear()
        exit_program = True

