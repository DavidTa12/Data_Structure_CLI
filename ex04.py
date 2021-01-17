from Finance import Budget

myBudget = Budget("ex03.json")

for category in myBudget.get_categories():
    print(category)
    myBudget.show_transactions(category)

