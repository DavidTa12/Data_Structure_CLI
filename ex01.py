def show_transactions(transactions_list: list):
    for i in transactions_list:
        print("You received", i, "euros") if i > 0 else print("You spent", i, "euros")


show_transactions([512, 42.08, -12])