from nested_data import albums

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][3]
    else:
        break
    print((albums[choice-1]))
