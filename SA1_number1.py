import requests

# URL of the raw dataset file on GitHub
url = 'https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
  
    # Save the content of the response to a file
    with open('words.txt', 'wb') as f:
        f.write(response.content)
        print('Dataset saved to file.')

    # A. Print the total number of words in the file.
    with open('words.txt', 'r') as file:
        words = file.read().split()
        total_words = len(words)
    print(f'\nTotal number of words in the file: {total_words}')

    # B. Print the longest word in the file.
    with open('words.txt', 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
    print(f'\nThe longest word in the file is: {longest_word}')

    # C. Print the number of words that start with a certain letter (use user input).
    def words_starting_with_letter(letter):
        with open('words.txt', 'r') as file:
            words = file.read().split()
            filtered_words = [word for word in words if word.startswith(letter)]
            return len(filtered_words)

    letter_input = input("\nEnter a letter to count words starting with that letter: ").strip().lower()

    if len(letter_input) == 1 and letter_input.isalpha():
        count = words_starting_with_letter(letter_input)
        print(f'Number of words starting with "{letter_input}": {count}')
    else:
        print('Please enter a single letter.')

    # D. Print all the words that contain a certain substring (use user input).
    def words_with_substring(substring):
        with open('words.txt', 'r') as file:
            words = file.read().split()
            filtered_words = [word for word in words if substring in word]
            for word in filtered_words:
                print(word)

    substring_input = input("\nEnter a substring to find words containing that substring: ").strip().lower()

    print('Words containing the substring:')
    words_with_substring(substring_input)

    # E. Print all the words that are palindromes (i.e., read the same backwards and forwards).
    def is_palindrome(word):
        return word == word[::-1]

    def print_palindromes():
        with open('words.txt', 'r') as file:
            words = file.read().split()
            palindrome_words = [word for word in words if is_palindrome(word)]
            for word in palindrome_words:
                print(word)

    print('\nPalindrome words in the file:')
    print_palindromes()

    # F. Count the frequency of each letter. 
    words_combined = ' '.join(words)
    character_frequency = {}

    for char in words_combined:
        character_frequency[char.lower()] = character_frequency.get(char.lower(), 0) + 1

    print('\nFrequency of each character:')
    for char in sorted(character_frequency):
        print(f'{char}: {character_frequency[char]}')

else:
    print('Failed to download dataset.')
