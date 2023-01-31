from nltk.corpus import words
import nltk
import random
word_list = words.words()

class Hangman:
    def __init__(self, word_list):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.list_letters = [] # List of letters that have already been tried
        self.__drawing = [
                        '_____  ',
                        '|   |  ',
                        '|      ',
                        '|      ',
                        '|      ',
                        '|      ',
                        '|      ',
                        '|______',
                        ]
        print(f'The mistery word has {len(self.word)} characters')
        print(self.word_guessed)
                        
    def __repr__(self):
        return '\n'.join(self.__drawing)

    def check_lives(self):
        if self.num_lives == 4:
            self.__drawing[2] = '|   O  '
        elif self.num_lives == 3:
            self.__drawing[3] = '| __|  '
            self.__drawing[4] = '|   |  '
        elif self.num_lives == 2:
            self.__drawing[3] = '| __|__'
        elif self.num_lives == 1:
            self.__drawing[5] = '|   /  '
            self.__drawing[6] = '|  /   '
        elif self.num_lives == 0:
            self.__drawing[5] = '|   /\ '
            self.__drawing[6] = '|  /  \\'
    
    def check_letter(self, letter):
        if letter in self.word.lower():
            if self.word.count(letter) > 1:
                idx = 0
                for _ in range(self.word.count(letter)):
                    idx = self.word.index(letter, idx)
                    self.word_guessed[idx] = letter
                    idx += 1
            idx = self.word.index(letter)
            self.word_guessed[idx] = letter
            self.num_letters -= 1
            print(self.word_guessed)
                
        else:
            self.num_lives -= 1
            self.check_lives()
            print(self)
        
        self.list_letters.append(letter)

    def ask_letter(self):
        while True:
            letter = input('Enter a character: ').lower()
            
            if letter in self.list_letters:
                print(f"{letter} was already tried")
            elif len(letter) > 1:
                print('Please, enter just one character')
            else:
                break

        self.check_letter(letter)

game = Hangman(word_list)

while True:
    game.ask_letter()
    if game.num_lives == 0:
        print(f'Sorry, the word was {game.word}')
        break
    elif game.num_letters == 0:
        print('Congratulations, you won!')
        break