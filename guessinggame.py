# import random
#
# highest = 10
# answer = random.randint(1, 10)
# print(answer)  # TODO: Remove after testing
#
# print ("Please guess number between 1 and {}: ".format(highest))
# guess = int(input())
#
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


import random

highest = 10
answer = random.randint(1, 10)
print(answer)
guess = None


while guess != answer:
    guess = int(input("Please guess number between 1 and {}: ".format(highest)))
    if guess == 0:
        break
    if guess == answer:
        print("Well done you guessed it")
        break
    elif guess < answer:
        print("Please guess lower")
    else:
        print("Please guess higher")



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

