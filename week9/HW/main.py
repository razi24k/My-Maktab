from package import game


my_game = game.Game()
while True:
    try:
        continue_game = input("Do you want to continue previous game results?(y/n): ")
        if continue_game == "y":
            my_game.load("./package/file.txt")
        elif continue_game == "n":
            pass
        else:
            raise TypeError
        rounds = int(input("How many rounds would you like to play with computer? "))
        for x in range(rounds):
            for i in range(3):
                choice = input("Please select one of the options r/p/s. ")
                res = my_game.play(choice)
                if res == "User":
                    my_game.u_wins += 1
                elif res == "Computer":
                    my_game.c_wins += 1
                else:
                    my_game.ties += 1
            if my_game.u_wins > my_game.c_wins:
                my_game.results["user wins"] += 1
            elif my_game.u_wins < my_game.c_wins:
                my_game.results["computer wins"] += 1
            else:
                my_game.results["ties"] += 1
            my_game.save(file_path="package/file.txt")
        print("rounds was finished...")
        print(f"result: {my_game.results}")
        exit_game = input("press exit to exit game and save results and any other key to restart game >> ")
        if exit_game.lower() == "exit":
            break
    except ValueError:
        print("Please enter an integer for rounds of game")
    except KeyboardInterrupt:
        print("finish")
        break
    except TypeError:
        print("Invalid input")

