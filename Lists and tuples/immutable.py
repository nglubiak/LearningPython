result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))

# Dołączenie elementu do stringa powoduje zmiane i tworzenia nowej wartości
# inne id

# Strings are immutable. When we tried to change a string, Python created
# a new object - a new string - and re-attached the name to it.
 



# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))
