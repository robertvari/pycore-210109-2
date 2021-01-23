import json, os

DATA_FILE = "phonebook.json"


def main():
    # get phonebook data from file if exists
    phonebook_data = get_phonebook_data()

    # get new data from user
    updated_phonebook = ask_user(phonebook_data)

    # save/update phonebook
    save_phonebook(updated_phonebook)


def get_phonebook_data() -> dict:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)

    return {}


def ask_user(phonebook_data):
    return {}


def save_phonebook(updated_phonebook):
    pass


if __name__ == '__main__':
    main()