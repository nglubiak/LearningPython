shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread"
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)



# Dołączenie elementu do listy bez zmiany tworzenia nowej listy
# to samo id

# Lists are mutable - they can be changed.
# When we appended a new item in this code, Python was able to
# change the contents of the list, without creating a new one.
