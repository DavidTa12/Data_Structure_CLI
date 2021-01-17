import json


class Budget:
    __transactions_list = {}

    def __init__(self, history_file_path=''):
        if history_file_path == '':
            print("No file specified")
        else:
            with open(history_file_path) as json_file:
                data = json.load(json_file)  # insert json content into data variable
                print(data)
                for transaction in data["transactions"]:
                    category = transaction["category"]
                    value = transaction["value"]
                    self.__transactions_list.update({category: value})  # transpose le format json en format Dict Python
                print(self.__transactions_list)

    def show_transactions(self, category):
        print("You received " + str(self.__transactions_list[category]) + " euros\n") if self.__transactions_list[
                                                                                             category] > 0 else print(
            "You spent " + str(self.__transactions_list[category]) + " euros\n")

    def add_transactions(self, transactions):
        # transactions must be a table of {"values": X, "category": "my_category"}
        try:
            for transaction in transactions:
                if not isinstance(transaction["value"], int) and not isinstance(transaction["value"], float):
                    print(str(transaction["value"]) + " is not an integer!")
                    raise ValueError(transaction)

            for transaction in transactions:
                self.__transactions_list.update({transaction["category"]: transaction["value"]})

        except ValueError:
            print("Reminder: only integers and floats are accepted as arguments")

    def get_categories(self):
        return self.__transactions_list.keys()  # fonction py qui permet retourner toutes les clefs sous forme tableau

#######################################################################################################


myBudget = Budget ("ex03.json")
# #print(myBudget.get_categories())
# myBudget.add_transactions([{"value" : 10, "category": "others"}, {"value" : -10, "category": "food"}])
for category in myBudget.get_categories():
    print(category)
    myBudget.show_transactions(category)
