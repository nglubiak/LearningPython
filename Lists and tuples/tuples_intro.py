albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bud Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))

for name, artist, year in albums:
    print("Album {}, Artist {}, Year{}"
          .format(name, artist, year))

print()

for name, artist, year in albums:
    print("Album {}, Artist {}, Year{}"
          .format(name, artist, year))









#
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bud Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# metallica[0] = "xyz"   -> is immutable

# Tuples are immutable and use parenthesis
# Lists are mutable and use square bracket

# metallica2=list(metallica)
# print(metallica2)
# # change the title
# metallica2[0] = "Master of Puppets"
# print(metallica2)

