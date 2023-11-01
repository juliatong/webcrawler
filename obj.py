import random
from abc import ABC, abstractmethod
import obj

class WordBank:
    def get_random_word(self, level):
        pass

    def get_challenge_level(self, level):
        pass

class AnimalWordBank(WordBank):
    word_bank = [["lion", "elephant", "giraffe", "tiger", "zebra"], [], []]

    def get_random_word(self, level):
        return random.choice(self.get_challenge_level(level))

    def get_challenge_level(self, level):
        return self.word_bank[level]

class WordBankFactory:
    @staticmethod
    def get_word_bank(theme):
        if theme.lower() == "animals":
            return AnimalWordBank()
        elif theme.lower() == "programming":
            # return ProgrammingWordBank()
            pass

        return AnimalWordBank()  # Default to animals

    


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CommandRepeat(Command):
    def __init__(self,  command_history, game_state):
        self.command_history=command_history
        self.game_state = game_state
        
    def execute(self):
        if len(self.command_history) > 0:
            repeat_guess=self.command_history[-1]
            self.command_history.append(repeat_guess)
            self.update_state(repeat_guess)
            

class CommandRedo(Command):
    def __init__(self,  undo_history, game_state):
        self.undo_history=undo_history
        self.game_state = game_state
          
    def execute(self):
        if len(self.undo_history) >0:
            current_guess=self.undo_history.pop()
            self.game_state.update_state(current_guess)
            


class CommandRegular(Command):
    def __init__(self, current_guess, command_history, game_state):
        self.current_guess = current_guess
        self.command_history = command_history
        self.game_state = game_state
        
        
    def execute(self):
        self.command_history.append(self.current_guess)
        self.game_state.update_state(self.current_guess)
        


        
class CommandUndo(Command):
    def __init__(self, command_history, undo_history):
        self.command_history = command_history
        self.undo_history=undo_history  
        
    def execute(self):
        if len(self.command_history) >0 :
            last_guess=self.command_history.pop()
            self.undo_history.append(last_guess)
            # TODOs: special reverse logic
            
                
class Invoker:
    def __init__(self, game_state):
        self.game_state = game_state


    def execute_command(self, command):
        if command:
            return command.execute()
        else:
            return None
        
        
        
       
class GameState:
    def __init__(self):
        self.command_history = []
        self.undo_history = []
        self.wrong_guess = ''
        self.correct_guess = ''
        self.word_bank = ['ant']
        self.secret_word = obj.WordBankFactory.get_word_bank().get_random_word().lower()
        self.unique_chars = self.hash_secret_word()
        self.guessing_word = '_' * len(self.secret_word)
        self.game_over = None 
        
          
    def update_state(self):
        if self.current_guess in self.unique_chars:
            self.correct_guess += self.current_guess
            for i in self.unique_chars[self.current_guess]: #fill_guessing_word
                self.guessing_word = self.guessing_word[:i] + self.current_guess + self.guessing_word[i+1:]
        else:
            self.wrong_guess += self.current_guess   