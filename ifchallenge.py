name = input("Please enter your name:")
age = int(input("How old are you {} ?".format(name)))
print(age)

if 18 <= age < 31:
    print("Welcome to the party")
else:
    print("You can't come in ")


# name = input("Please enter your name:")
# age = int((input("How old are you ?")))
#
# if 18 <= age < 31:
#     print("Welcome to club 18-30 holidays, {0}".format(name))
# else:
#     print("I am sorry, our holidays are only for cool people")