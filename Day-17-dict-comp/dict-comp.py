# {key: expression for key, value in iterable}

# Without dictionary comprehension
# squares_dict = {}
#
# for i in range(1, 6):
#     squares_dict[i] = i**2
#
# print(squares_dict)

# # With dictionary comprehension
# squares_dict = {i: i**2 for i in range(1, 6)}
#
# print(squares_dict)

# squares_dict = {i: i**2 for i in range(1, 6)}
# print(squares_dict)
# # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 2. Word Length Dictionary

# words = ['apple', 'banana', 'cherry']
# lengths_dict = {word: len(word) for word in words}
# print(lengths_dict)

# Output: {'apple': 5, 'banana': 6, 'cherry':


# 3. Filter a Dictionary

# fruit_prices = {'apple': 3, 'banana': 1, 'cherry': 5, 'kiwi': 2}
# expensive_fruits = {fruit: price for fruit, price in fruit_prices.items() if fruit == 'apple' or fruit == 'banana'}
# print(expensive_fruits)

# # Output: {'apple': 3, 'cherry': 5}


# -----------------------------------------------------------------------------

# cities_in_f = {
#     'Lahore': 100,
#     'Dera Ismail Khan': 110,
#     'Karachi': 170
# }
#
# cities_in_C = {key: round((value-32)*(5/9), 2) for key, value in cities_in_f.items()}
#
#
# print(cities_in_C)


# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
#
# # sunny_weather = {key: value for key, value in weather.items() if value == "sunny"}
# #
# list_comp = [value for key, value in weather.items()]
# print(list_comp)


# weather = {'New York': 40, 'Boston': 100, 'Los Angeles': 20, 'Chicago': 32}
#
# # {key: (if/else) for (key,value) in weather.items()}
#
# desc_weather = {key: ('sunny' if value >= 40 else "snowing") for (key, value) in weather.items()}
#
#
# print(desc_weather)

# 1. Unique Square Numbers

# squares_set = {i**2 for i in range(1, 10)}
# # print(type(squares_set))
# print(squares_set)


# 2. Extract Unique Vowels from a String

# sentence = "comprehension is amazing"
# vowels_set = {char for char in sentence if char in 'aeiou'}
# print(vowels_set)
#

# Output: {'o', 'i', 'a', 'e'}

# 3. Filter Even Numbers into a Set

# even_numbers_set = {i for i in range(1, 21) if i % 2 == 0}
# print(even_numbers_set)

# Output: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}


# Step 1: Ask the user to input a sentence
sentence = input("Enter a sentence: ")

# Step 2: Create a list of words using list comprehension
words = sentence.split()

# Step 3: Count the frequency of each word using a dictionary
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Step 4: Filter out words that appear only once using a list comprehension
frequent_words = [word for word in word_count if word_count[word] > 1]

# Step 5: Print the list of words that appear more than once
print(frequent_words)


