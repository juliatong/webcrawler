import random
HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

class Hangman:
    def __init__(self):                 
        print('HANGMAN GAME')    
        self.reset_game()

    def reset_game(self):
        self.wrong_guess = ''
        self.correct_guess = ''
        self.word_bank = ['ant']
        self.secret_word = self.select_random_word(self.word_bank)
        self.unique_chars = self.hash_secret_word(self.secret_word)
        self.guessing_word = '_' * len(self.secret_word)
        self.game_over = False

    def select_random_word(self, word_bank):
        word_index = random.randint(0, len(word_bank) - 1)
        return word_bank[word_index]

    def get_valid_guess(self, all_guess):
        while True:
            print('Please guess a letter.')
            guess = input().lower()
            if len(guess) != 1:
                print('Please enter a non-empty single letter.')
            elif guess in all_guess:
                print('You have already guessed that letter. Choose a different letter.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a valid letter.')
            else:
                return guess

    def play_again(self):
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def fill_guessing_word(self, current_guess):
        for i in self.unique_chars[current_guess]:
            self.guessing_word = self.guessing_word[:i] + current_guess + self.guessing_word[i+1:]
        return self.guessing_word   

    def display_current_board(self):
        print(HANGMAN_PICS)
        for letter in self.guessing_word:
            print(letter, end=' ')

    def hash_secret_word(self, secret_word):
        char_to_indices = {}
        for index, c in enumerate(secret_word):
            if c in char_to_indices:
                char_to_indices[c].append(index)
            else:
                char_to_indices[c] = [index]
        return char_to_indices


    def play_game(self):
        while True: 
            while True:
                self.display_current_board()
                current_guess = self.get_valid_guess(self.wrong_guess + self.correct_guess)
                        
                if current_guess in self.unique_chars:
                    self.correct_guess += current_guess
                    self.fill_guessing_word(current_guess)
                    if self.guessing_word == self.secret_word:
                        self.game_over = True
                        print('Yes, the secret word is ' + self.secret_word + '. You have won!')
                        break
                else:
                    self.wrong_guess += current_guess
                    if len(self.wrong_guess) == len(HANGMAN_PICS):
                        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1])
                        print('You have run out of guesses.\n After ' + str(len(self.wrong_guess)) + ' wrong guesses and ' + str(len(self.correct_guess)) + ' correct guesses, the word is "' + self.secret_word + '"')
                        self.game_over = True
                        break
                print('The current guessing word after filling is: ' + self.guessing_word)
                    
            if self.game_over:
                if self.play_again():
                    self.reset_game()
                else:
                    break
                
my_game = Hangman()
my_game.play_game()
         

            
        

