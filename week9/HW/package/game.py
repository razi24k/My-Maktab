import random
import pickle


class File:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class Game:
    results = {
        "user wins": 0,
        "computer wins": 0,
        "ties": 0
    }

    def __init__(self):
        self.u_wins = 0
        self.c_wins = 0
        self.ties = 0

    @staticmethod
    def play(u_choice):
        computer_choice = str(random.choice(("r", "p", "s")))
        # print(computer_choice)
        if u_choice in ('r', 'p', 's'):
            if computer_choice == u_choice:
                return "Tie"
            else:
                if (computer_choice == "r") and (u_choice == "p"):
                    return "User"
                elif computer_choice == "p" and u_choice == "s":
                    return "User"
                elif computer_choice == "s" and u_choice == "r":
                    return "User"
                else:
                    return "Computer"
        else:
            print("wrong choice!")

    @classmethod
    def load(cls, file_path):
        with File(file_path, "rb") as _:
            cls.results = pickle.load(_)

    @classmethod
    def save(cls, file_path):
        with File(file_path, "wb") as _:
            pickle.dump(cls.results, _)
