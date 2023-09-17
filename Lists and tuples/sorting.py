pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

# różnica między funkcją sort i sorted. Sort nadpisuje listę, a sorted tworzy nową i ją sortuje
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

# wypisze Null:
another_sorted_numbers = numbers.sort()
print(numbers)
print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jump over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort(key=str.casefold)
print(names)
