pangram = """The quick brown fox jumps\tover the lazy dog"""

words = pangram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(", "))

# value = "".join(char if char not in separator else " " for char in numbers).split()

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7'
                  ]
values = "".join(generated_list)
print(values)


values_list = values.split()
print(values_list)


# JOIN
#  That means the items in the list won't be separated from each other
#  by anything. Remember that the string you use when calling join,
#  is used to separate the items that you're joining.

# SPLIT
# "split" will split on whitespace, and we can see the spaces in the string, on the last line of our output.
# split - splits up the string at the spaces



# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# 1st way: replace the value in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)

# 2nd way: create a new value
integer_value = []
for value in values_list:
    integer_value.append(int(value))

print(integer_value)




