shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue
#
#     print("Buy " + item)


# Usually the situation where continue is necessary/useful, is when you want to skip the remaining code in the loop and continue iteration.
#
# I don't really believe it's necessary, since you can always use if statements to provide the same logic, but it might be useful to increase readability of code.

for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)
