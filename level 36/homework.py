# 2) Find the position of the first occurrence of the word "Python" in a sentence.
sentence = "goa is best"
position = sentence.find("Python")
print("The position of the first occurrence of the word 'Python' is:", position)
# 3) Search for a user-specified substring in a provided string and print its starting index.
def find_substring(main_string, substring):
    position = main_string.find(substring)
    if position != -1:
        print(f"The substring '{substring}' is found at index: {position}")
    else:
        print(f"The substring '{substring}' is not found in the provided string.")

main_string = "goa is best"
substring = "Python"
find_substring(main_string, substring)
# 4) Write a function to find and return the index of a specified character in a given string.
def find_character_index(main_string, character):
    position = main_string.find(character)
    if position != -1:
        return position
    else:
        return "Character not found in the provided string."

main_string = "goa is best"
character = "P"
index = find_character_index(main_string, character)
print(f"The index of the character '{character}' is: {index}")
def count_word_the(paragraph):
    words = paragraph.lower().split()
    count = words.count("the")
    return count

paragraph = "goa is best"
count = count_word_the(paragraph)
print(f"The word 'the' appears {count} times in the paragraph.")
