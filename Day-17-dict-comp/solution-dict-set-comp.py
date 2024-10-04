# nested_dict = {i: {'square': i**2, 'cube': i**3} for i in range(1, 6)}
# print(nested_dict)

# sentence1 = input("Enter the first sentence: ").lower().split()
# sentence2 = input("Enter the second sentence: ").lower().split()
#
# common_words = {word for word in sentence1 if word in sentence2}
# print(common_words)


# names = ['Alice', 'Bob', 'Charlie', 'Dave']
# scores = [85, 92, 78, 88]
#
# if len(names) == len(scores):
#     student_scores = {names[i]: scores[i] for i in range(len(names))}
#     print(student_scores)
# else:
#     print("The lists do not match in length.")


# sentence = input("Enter a sentence: ")
# frequency_dict = {char: sentence.count(char) for char in set(sentence) if char != ' '}
# print(frequency_dict)
#
#
# num_dict = {i: ('Even' if i % 2 == 0 else 'Odd') for i in range(1, 21)}
# even_numbers = {key: value for key, value in num_dict.items() if value == 'Even'}
# print(even_numbers)


students = {
    'Alice': {'Math': 85, 'Science': 90},
    'Bob': {'Math': 75, 'Science': 60},
    'Charlie': {'Math': 45, 'Science': 40},
    'Dave': {'Math': 80, 'Science': 85},
    'Eve': {'Math': 55, 'Science': 70},
}

# 2. Add average score to each student's dictionary
students_with_avg = {name: {**scores, 'average': (scores['Math'] + scores['Science']) / 2} for name, scores in students.items()}

# 3. Identify students who scored an average of 80 or more
high_achievers = {name for name, scores in students_with_avg.items() if scores['average'] >= 80}
#
# 4. Filter out students who failed in either subject
passed_students = {name: scores for name, scores in students_with_avg.items() if scores['Math'] >= 50 and scores['Science'] >= 50}

print(f"Students with Average Scores: {students_with_avg}")
print(f"High Achievers (80+ Average): {high_achievers}")
print(f"Passed Students: {passed_students}")

