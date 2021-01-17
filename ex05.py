from Finance import Budget
import json

CONSULT_BALANCE = 1
ADD_TRANSACTION = 2
CONSULT_TRANSACTION_HIST = 3
QUIT_MENU = 4

transactions_file = "transactions.json"


def main():
    user_choice = 0
    my_budget = Budget(transactions_file)

    while user_choice != QUIT_MENU:  # while user input != QUIT_MENU, program must be running
        display_main_menu()
        user_choice = int(input())  # selon valeur de l'input

        if user_choice == CONSULT_BALANCE:
            consult_balance(my_budget)

        elif user_choice == ADD_TRANSACTION:
            add_transaction(my_budget)

        elif user_choice == CONSULT_TRANSACTION_HIST:
            consult_transactions_hist(my_budget)

        elif user_choice == QUIT_MENU:
            exit_program(my_budget, transactions_file)


def display_main_menu():
    print("Choose between: ")
    print("1 - consult my balance")
    print("2 - add new transaction")
    print("3 - consult your transactions history")
    print("4 - quit")


def consult_balance(my_budget):
    debit = 0
    credit = 0
    balance = 0
    # pour toutes les transactions, je fais le calcul du débit, crédit et solde
    for category in my_budget.get_transactions():
        if my_budget.get_transactions()[category] < 0:
            debit += my_budget.get_transactions()[category]

        else:
            credit += my_budget.get_transactions()[category]

        balance += my_budget.get_transactions()[category]

    print("Total debit = " + str(debit))
    print("Total credit = " + str(credit))
    print("Total balance = " + str(balance))

    x = input("Enter \"exit\" to exit\n")
    if x == "exit": return


def add_transaction(my_budget):
    category = input("Enter category: \n")  # demande une entrée user de la catégorie à ajouter
    value = input("Enter " + category + " value: \n")  # demande une entrée user de la valeur à ajouter
    transactions_to_add = []  # tableau car méthode add_transactions attend un tableau d'objets json
    new_transaction = {"category": category, "value": int(value)}  # objet
    transactions_to_add.append(new_transaction)  # tableau auquel j'ajoute l'objet

    my_budget.add_transactions(transactions_to_add)

    print("transaction was successfully added")

    return


def consult_transactions_hist(my_budget):
    for category in my_budget.get_categories():
        print(category)
        my_budget.show_transactions(category)

    x = input("Enter \"exit\" to exit\n")
    if x == "exit": return


def save_data_to_file(my_budget, transactions_file):
    data = {}
    transactions = []
    for key in my_budget.get_transactions():
        transactions.append(
            {"value": my_budget.get_transactions()[key], "category": key})  # transforme Dict sous forme json

    data['transactions'] = transactions

    with open(transactions_file, 'w') as outfile:  # écrit les données dans le fichier json en annule et remplace
        json.dump(data, outfile)

    print("transaction was successfully saved")


def exit_program(my_budget, transactions_file):
    save_data_to_file(my_budget, transactions_file)
    print("Exiting program \n")


main()
