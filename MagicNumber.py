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
    magic_number = random.randint(0, 10)
    max_tries = 3

    user_number = get_user_number()


def get_user_number() -> int:
    user_number = int(input("Your number?"))
    return user_number


if __name__ == '__main__':
    main()