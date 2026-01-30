def compute_average(numbers):
    return sum(numbers) / len(numbers)

def compare_length_and_average(word_length, average):
    if word_length > average:
        print(f"The length of the word is greater than the average.")
    elif word_length < average:
        print(f"The length of the word is less than the average.")
    else:
        print(f"The length of the word is equal to the average.")

word = input("Enter a word: ")
word_length = len(word)

numbers = []
for i in range(word_length):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

average = compute_average(numbers)

print(numbers)
print(f"The length of the word is {word_length}")
print(f"The average of the numbers is {average}")

compare_length_and_average(word_length, average)