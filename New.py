for x in range(30):
    if x % 3 != 0 and x % 5 != 0:
        continue
    print(x)




# import random
#
# highest = 10
# answer = random.randint(1, 10)
# print(answer)
# guess = None
#
#
# while guess != answer:
#     guess = int(input("Please guess number between 1 and {}: ".format(highest)))
#     if guess == 0:
#         break
#     if guess == answer:
#         print("Game over")
#         break
#     elif guess < answer:
#         print("Za mao")
#     else:
#         print("Za duzo")





# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# # Use a for loop and an if statement to print just the capitals in the quote above.
#
# for char in quote:
#     if char.isupper():
#         print(char)





