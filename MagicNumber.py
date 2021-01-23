import random

USER_CREDITS = 0


def main():
    print("-"*50, "Magic Number", "-"*50)
    print(f"Your credits: {USER_CREDITS}\n")

    if USER_CREDITS < 0:
        print("You lost all your credits. Try again later :(")
        exit()

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
    print(f"DEBUG: {magic_number}")
    max_tries = 3

    user_number = get_user_number()

    while user_number != magic_number:
        max_tries -= 1
        if max_tries == 0:
            print("You lost the game")
            update_credits(-10)
            main()

        print(f"Wrong number. You have {max_tries} more tries.")
        user_number = get_user_number()

    print(f"You win! My number was {magic_number}")
    update_credits(10)
    main()


def get_user_number() -> int:
    user_number = int(input("Your number?"))
    return user_number


def update_credits(value):
    global USER_CREDITS
    USER_CREDITS += value


if __name__ == '__main__':
    main()