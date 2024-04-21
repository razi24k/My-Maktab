import os


def clear():
    os.system('cls' if os.name.lower() == 'nt' else 'clear')


class Menu:
    def __init__(self):
        self.rounds = 3
        self.main_choice = self.main_menu
        self.customize_choice = self.play_menu
        self.player1_sign = "X"
        self.player2_sign = "O"

    def main_menu(self):
        print(f'''{"Main Menu".center(42, "*")}
*{"1. Play Game".center(40)}*
*{"2. Customize Settings".center(40)}*
*{"3. Exit".center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        main_user_choice = input(" ")
        return main_user_choice

    def play_menu(self):
        print("*" * 44)
        print(f'''*{"1. customize your char in game".center(42)}*
*{"2. customize number of rounds".center(42)}*
*{"3. back to main menu".center(42)}*''')
        print("*" * 44)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice


class Table:
    white_list = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]

    def __init__(self) -> None:
        self.map = {n: n + 1 for n in range(10)}

    def check(self):
        for li in self.white_list:
            if self.map[li[0] - 1] == self.map[li[1] - 1] == self.map[li[2] - 1]:
                return True

    def print(self):
        print("""
        -------------------
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        """.format(
            *[self.map[j] for j in self.map]
        ))

    def mark(self, cell_no, sign):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Invalid Cell number"
        assert not self.map[cell_no - 1] in ('o', 'x'), "Cell is filled"

        self.map[cell_no - 1] = sign.lower()


class Setting:
    round_counter = 0

    def __init__(self, rounds):
        self.winners = []
        self.round = rounds

    def win(self):
        if self.winners.count(Player.players[0]) > self.winners.count(Player.players[1]):
            return Player.players[0].name
        elif self.winners.count(Player.players[0]) < self.winners.count(Player.players[1]):
            return Player.players[1].name
        else:
            return f'{Player.players[1]} = {Player.players[0]}'

    def run(self):
        loop_count = 0
        table = Table()
        Setting.round_counter += 1
        while loop_count < 9:
            loop_count += 1
            clear()
            for player in Player.players:
                clear()
                print(f"Round {Setting.round_counter} of {self.round}".center(33, "_"))
                table.print()
                print(self.winners)

                cell_no = int(input(f"{player.name}[{player.sign}]: Enter cell no (1, 9): "))
                table.mark(cell_no, player.sign)

                if table.check():
                    clear()
                    print(f"{player.name} is win ^-0")
                    setting.winners.append(player.name)
                    table.print()
                    return


class Player:
    players = []

    def __init__(self, name):
        self.name = name
        self.sign = None
        self.players.append(self)


# start:
print("---------------------------------")
print("| Welcome to Maktab 112 XO Game |")
print("---------------------------------")
input("Please Enter To Start New Game... ")
clear()
player_name1 = input("> Enter player (1) name: ")
player_1 = Player(player_name1)
player_name2 = input("> Enter player (2) name: ")
player_2 = Player(player_name2)
start_game = False
my_menu = Menu()
while not start_game:
    clear()
    main_menu_str = my_menu.main_choice()
    main_menu_str = str(main_menu_str)
    print("started")
    if main_menu_str == "1":
        print("your choice is 1")
        player_1.sign = my_menu.player1_sign
        player_2.sign = my_menu.player2_sign
        print('start')
        start_game = True
        break

    elif main_menu_str == "2":
        clear()
        play_menu_str = my_menu.play_menu()
        play_menu_str = str(play_menu_str)
        if play_menu_str == "1":
            clear()
            my_menu.player1_sign = input(f"> Enter player {player_name1}'s char: ")
            my_menu.player2_sign = input(f"> Enter player {player_name2}'s char: ")
            print(f"Characters changed successfully")
            print(f"\n{player_name1.title()}: '{my_menu.player1_sign}', \t{player_name2.title()}: '{my_menu.player2_sign}'")
            input("Press enter to back to menu ...")
        elif play_menu_str == "2":
            clear()
            number_of_rounds = int(input("> Enter number of rounds: "))
            my_menu.rounds = number_of_rounds
            print(f"rounds changed successfully\nNumber of rounds: {number_of_rounds}")
            input("Press enter to back to menu ...")
        elif play_menu_str == "3":
            clear()
            pass
    elif main_menu_str == "3":
        break
setting = Setting(my_menu.rounds)

for i in range(setting.round):
    setting.run()

winner = setting.win()
print(winner)
