age = int(input("How old are you? "))

# if age >= 16 and age <=65:
# if 16 <= age <= 65:
if age in range (16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-"*80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")


# When comparing conditions using and, Python will stop checking as soon as it finds a condition that is FALSE.
# When comparing conditions using or, it will stop as soon as it finds one that is TRUE.