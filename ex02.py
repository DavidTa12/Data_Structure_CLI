class Budget:
    __transactions_list = []

    def show_transactions(self):
        for i in self.__transactions_list:
            print("You received " + str(i) + " euros") if i > 0 else print("You spent " + str(i) + " euros")

    def add_transactions(self, transactions):
        try:
            for transaction in transactions:  # vérifie que tous les params sont des int ou float
                if not isinstance(transaction, int) and not isinstance(transaction, float):
                    print(str(transaction) + " is not an integer!")
                    raise ValueError(transaction)

            for transaction in transactions:  # tout est OK, ajout dans l'attribut __transactions_list
                self.__transactions_list.append(transaction)

        except ValueError:
            print("Reminder: only integers and floats are accepted as arguments")


myBudget = Budget()
# myBudget.add_transactions([512, 42.08, -12, "a"])
myBudget.add_transactions([512, 42.08, -12])
myBudget.show_transactions()
