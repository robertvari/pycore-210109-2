import json, os

DATA_FILE = "phonebook.json"


def main():
    menu()


def menu():
    menu_string = "1. Add new phone number.\n2. Exit"
    print(menu_string)

    user_input = input()

    if user_input == "1":
        # get phonebook data from file if exists
        phonebook_data = get_phonebook_data()

        # get new data from user
        updated_phonebook = ask_user(phonebook_data)

        # save/update phonebook
        save_phonebook(updated_phonebook)

        menu()
    else:
        print("Goodbye!")
        exit()


def get_phonebook_data() -> dict:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)

    return {}


def ask_user(phonebook_data):
    name = input("Name:")
    address = input("Address:")
    phone = input("Phone:")

    phonebook_data[phone] = {
        "name": name,
        "address": address
    }

    return phonebook_data


def save_phonebook(updated_phonebook):
    with open(DATA_FILE, "w") as f:
        json.dump(updated_phonebook, f)

    print("Data saved!")


if __name__ == '__main__':
    main()