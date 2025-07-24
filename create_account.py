import random
import os

class Account:
    def __init__(self, user_id, first_name, last_name, email):
        self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email


    def set_first_name(self, first_name):
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_email(self, email):
        self.__email = email

    def get_user_id(self):
        return self.__user_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_email(self):
        return self.__email

    def to_string(self):
        userid = self.get_user_id()
        first_name = self.get_first_name()
        last_name = self.get_last_name()
        email = self.get_email()
        return f"{userid},{first_name},{last_name},{email}\n"

def generate_unique_id(filename="information_database.txt"):
    used_ids = set()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                user_id = line.strip().split(",")[0]
                used_ids.add(user_id)

    while True:
        unique_id = str(random.randint(10000, 99999))
        if unique_id not in used_ids:
            return unique_id

def save_account_to_txt(account, filename="information_database.txt"):
    with open(filename, "a") as f:
        f.write(account.to_string())

def create_account():
    first_name = input("Please enter your first name: ").strip()
    last_name = input("Please enter your last name: ").strip()
    email = input("Please enter your email address: ").strip()

    user_id = generate_unique_id()
    new_account = Account(user_id, first_name, last_name, email)
    save_account_to_txt(new_account)

    print(f"Account created! Your User ID is: {new_account.get_user_id()}\n")

if __name__ == "__main__":
    create_account()