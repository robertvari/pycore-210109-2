import random


def main():
    print("-"*50, "Magic Number", "-"*50)

    user_choice = menu()

    if user_choice == "1":
        # start game
        game()
    else:
        print("Goodbye!")
        exit()


def menu():
    choices = "1. New Game\n2. Exit Game"
    print(choices)
    return input()


def game():
    pass


if __name__ == '__main__':
    main()