a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)
# There is unpacking a tuple
print("Unpacking a tuple")

data = 1, 2, 76
x, y, z = data       # -> zawsze odpakowanie sie powiedzie
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]
# data_list.append(15)   -> nie moze odpakowac 4 cyfry
p, q, r = data_list
print(p)
print(q)
print(r)


