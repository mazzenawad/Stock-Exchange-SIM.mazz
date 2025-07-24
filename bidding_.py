import os

class Bidding:
    def __init__(self, ticker_name, bidding_price, amount, user_id):
        self.__ticker_name = ticker_name
        self.__bidding_price = bidding_price
        self.__amount = amount
        self.__user_id = user_id

    def set_ticker_name(self, ticker_name):
        self.__ticker_name = ticker_name
    def set_bidding_price(self, bidding_price):
        self.__bidding_price = bidding_price
    def set_amount(self, amount):
        self.__amount = amount
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_ticker_name(self):
        return self.__ticker_name
    def get_bidding_price(self):
        return self.__bidding_price
    def get_amount(self):
        return self.__amount
    def get_user_id(self):
        return self.__user_id

    def __str__(self):
        return f"{self.get_ticker_name()},{self.get_bidding_price()},{self.get_amount()},{self.get_user_id()}\n"

def is_valid_user_id(user_id, filename="information_database.txt"):
    if not os.path.exists(filename):
        return False
    with open(filename, "r") as f:
        for line in f:
            if line.strip().split(",")[0] == user_id:
                return True
    return False

def save_bidding_to_txt(bid, filename="biding_database.txt"):
    with open(filename, "a") as f:
        f.write(bid.__str__())

def overwrite_asking_db(data, filename="asking_database.txt"):
    with open(filename, "w") as f:
        for line in data:
            f.write(line)

def execute_order(ticker_name, amount, price, bid_user_id, ask_user_id, filename="executed_orders.txt"):
    with open(filename, "a") as f:
        f.write(f"{ticker_name},{amount},{price},{bid_user_id},{ask_user_id}\n")
    print(f"{amount} order(s) successfully has been executed at {price}")

def create_bidding():
    print("STOCK BIDDING")
    ticker_name = str(input("Enter the name of the company: ").strip())
    bidding_price = float(input("Provide your bidding price: "))
    amount = int(input("Provide the amount of stocks you want to buy: "))
    user_id = str(input("Enter your user ID: ").strip())

    while not is_valid_user_id(user_id):
        print("Invalid User ID.")
        print("Type 'create' to make a new account.")
        user_id = input("Please provide your userID (xxxxx): ").strip()
        if user_id.lower() == "create":
            os.system('python create_account.py')

    new_bid = Bidding(ticker_name, bidding_price, amount, user_id)

    matched = False
    if os.path.exists("asking_database.txt"):
        with open("asking_database.txt", "r") as f:
            asks = [line.strip().split(",") for line in f.readlines()]

        updated_asks = []
        for ask in asks:
            ask_stock, ask_price, ask_amount, ask_user_id = ask
            ask_price = float(ask_price)
            ask_amount = int(ask_amount)

            if ask_stock == ticker_name and bidding_price >= ask_price:
                matched = True
                if amount == ask_amount:
                    execute_order(ticker_name, amount, bidding_price, user_id, ask_user_id)
                    amount = 0
                elif amount < ask_amount:
                    execute_order(ticker_name, amount, bidding_price, user_id, ask_user_id)
                    ask_amount -= amount
                    updated_asks.append(f"{ask_stock},{ask_price},{ask_amount},{ask_user_id}\n")
                    amount = 0
                else:
                    execute_order(ticker_name, ask_amount, bidding_price, user_id, ask_user_id)
                    amount -= ask_amount
                    continue
                break

        if amount > 0:
            remaining_bid = Bidding(ticker_name, bidding_price, amount, user_id)
            save_bidding_to_txt(remaining_bid)
        overwrite_asking_db(updated_asks)
    else:
        save_bidding_to_txt(new_bid)

    if not matched:
        print("No matching ask found. Your bid has been recorded.")

if __name__ == "__main__":
    create_bidding()
