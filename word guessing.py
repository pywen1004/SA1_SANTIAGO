import random
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
else:
    print('Failed to download dataset.')

# Function to randomly select a word from the "words.txt" file
def select_word():
    with open('words.txt', 'r') as f:
        words = f.readlines()
    return random.choice(words).strip().lower()

# Function to display the word to the player
def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

# Function to get the player's guess
def get_guess():
    while True:
        guess = input('Enter a letter: ').strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print('Invalid input. Please enter a single letter.')

# Main function to run the game
def main():
    print('Welcome to the Word Guessing Game!')
    word = select_word()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    while True:
        print('\n' + display_word(word, guessed_letters))
        guess = get_guess()

        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts += 1
            print(f'Incorrect guess! {max_attempts - attempts} attempts left.')
            if attempts >= max_attempts:
                print(f'You ran out of attempts. The word was "{word}". Game over!')
                break
        else:
            if all(letter in guessed_letters for letter in word):
                print(f'Congratulations! You guessed the word "{word}" correctly!')
                break

# Call the main function to run the game
if __name__ == '__main__':
    main()
