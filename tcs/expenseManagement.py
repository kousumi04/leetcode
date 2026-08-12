totalIncome=int(input("Enter total income:"))
totalExpense=0
breakdown={}
while True:
    category=input("Enter category:")
    if category=="done":
        break
    expense=int(input("Enter expense:"))
    totalExpense+=expense
    if category in breakdown:
        breakdown[category]+=expense
    else:
        breakdown[category]=expense
totalSavings=totalIncome-totalExpense
print("Total Income:", totalIncome)
print("Total Expenses:", totalExpense)
print("Total Savings:", totalSavings)

print("Category Breakdown:")
for category in breakdown:
    print(category, breakdown[category])         
# total income total expense
# total savings, breakdown of each categories