import obj
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
        self.game_state=obj.GameState()
        

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


    def display_current_board(self):
        print(HANGMAN_PICS[len(self.wrong_guess)])
        for letter in self.guessing_word:
            print(letter, end=' ')

    def hash_secret_word(self):
        char_to_indices = {}
        for index, c in enumerate(self.secret_word):
            if c in char_to_indices:
                char_to_indices[c].append(index)
            else:
                char_to_indices[c] = [index]
        return char_to_indices


    def evaluateResult(self):
        if self.guessing_word == self.secret_word:
            game_over = True
            print('Yes, the secret word is ' + self.secret_word + '. You have won!')
            return game_over
        if len(self.wrong_guess) == len(HANGMAN_PICS):
            print(HANGMAN_PICS[len(HANGMAN_PICS) - 1])
            print('You have run out of guesses.\n After ' + str(len(self.wrong_guess)) + ' wrong guesses and ' + str(len(self.correct_guess)) + ' correct guesses, the word is "' + self.secret_word + '"')
            game_over = True
            return game_over
    
        
    def play_game(self):
        while True:
            self.display_current_board()
            
            invoker = obj.Invoker()
            self.current_guess = self.get_valid_guess(self.wrong_guess + self.correct_guess)
            do_command = obj.CommandRegular(self.current_guess)
            
            undo_command = obj.CommandUndo(invoker.command_history)
            redo_command = obj.CommandRedo(invoker.undo_history)
            repeat_command = obj.CommandRepeat(invoker.command_history)

            invoker.execute_command(do_command)
            invoker.execute_command(undo_command)     
            invoker.execute_command(redo_command)     
            invoker.execute_command(repeat_command)     
                    
            
            self.evaluateResult()
                
            if self.game_over:
                if self.play_again():
                    self.game_state = obj.GameState()
                else:
                    break
                
my_game = Hangman()
my_game.play_game()
         

            
        

