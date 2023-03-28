# Python simple Project: Text Analysis

#  This program analyses a given text and provides some insights about it using String Methods.

# Step 1: Get the input from the user
text = input("Enter the text: ")

# Step 2 : Analyse the text using string methods

# Count the number of characters in the text
num_chars = len(text)

# Count the number of words in the text
num_words = len(text.split())

# Count the number of sentences in the text
num_sentences = text.count('.')+text.count('?')+text.count('!')

# Convert the first character of each word capitalized
char_capitalized = text.title()

#step 3: Display the results to the user

print("Text Analysis:")
print("Number of characters:",num_chars)
print("Number of words:",num_words)
print("Number of sentences:",num_sentences)
print("First Char as capitalized:",char_capitalized)


