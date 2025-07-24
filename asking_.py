import os

class Asking:
    def __init__(self, stock_ticker, asking_price, amount, user_id):
        self.__stock_ticker = stock_ticker
        self.__asking_price = asking_price
        self.__amount = amount
        self.__user_id = user_id

    def set_stock_ticker(self, stock_ticker):
        self.__stock_ticker = stock_ticker
    def set_asking_price(self, asking_price):
        self.__asking_price = asking_price
    def set_amount(self, amount):
        self.__amount = amount
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_stock_ticker(self):
        return self.__stock_ticker
    def get_asking_price(self):
        return self.__asking_price
    def get_amount(self):
        return self.__amount
    def get_user_id(self):
        return self.__user_id

    def __str__(self):
        return f"{self.get_stock_ticker()},{self.get_asking_price()},{self.get_amount()},{self.get_user_id()}\n"

def save_asking_to_txt(asking, filename="asking_database.txt"):
    with open(filename, "a") as f:
        f.write(asking.__str__())

def validate_user(user_id, filename="information_database.txt"):
   
    if not os.path.exists(filename):
        return False

    with open(filename, "r") as f:
        for line in f:
            if line.strip().split(",")[0] == user_id:
                return True
    return False

def create_asking():
    print("STOCK ASKING")
    stock_ticker = str(input("Enter the name of the company: ").strip())
    asking_price = float(input("Provide your asking price: "))
    amount = int(input("Provide the number of stocks you want to sell: "))
    user_id = str(input("Enter your userID (xxxxx): ").strip())
    
    while not validate_user(user_id):
        print("Invalid User ID.")
        print("Type 'create' to make a new account.")
        user_id = input("Please provide your userID (xxxxx): ").strip()
        if user_id.lower() == "create":
            os.system('python create_account.py')

    new_asking = Asking(stock_ticker, asking_price, amount, user_id)
    save_asking_to_txt(new_asking)

    print("Your stock asking has been recorded.")

if __name__ == "__main__":
    create_asking()
