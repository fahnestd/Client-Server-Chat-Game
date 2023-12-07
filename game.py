import random

# Citation: https://inventwithpython.com/invent4thed/chapter8.html
# Adapted some of the code and used the ascii images of hangman.

class Game:
    words = ['galaxy', 'nebula', 'cosmos', 'asteroid', 'comet', 'orbit', 'quasar', 'celestial', 'supernova', 'blackhole', 'constellation', 'exoplanet', 'astronomy', 'gravity', 'meteoroid', 'satellite', 'interstellar', 'stellar', 'cosmic', 'parallax']

    word = ''
    wordLetters = []

    letters = []
    letterset = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        self.chooseWord()

    def choice(self, choice):
        if len(choice) == 1:
            if not self.guessLetter(choice):
                return (False, 'Invalid Guess, please try again!')
            return (False, '')
        else:
            return (True, self.guessWord(choice))

    def chooseWord(self):
        self.word = self.words[random.randint(0, len(self.words) - 1)]
        self.wordLetters = set(self.word)        

    def guessWord(self, word):
        if word == self.word:
            return f"{self.word}\n{self.getHangmanPicture()}\n\nYou Won!"
        else:
            return f"{self.word}\n{self.getHangmanPicture()}\n\nYou Lost!"

    def guessLetter(self, letter):
        if letter not in self.letterset or letter in self.letters:
            return False

        self.letters.append(letter)


    def checkForWin(self):
        #check if the all letters were guessed correctly by comparing letter sets.
        # Citation https://www.geeksforgeeks.org/python-intersection-two-lists/
        return len(list(set(self.wordLetters) & set(self.letters))) == len(self.wordLetters)

    def getSensoredWord(self):
        sensored = ''
        for letter in self.word:
            if letter in self.letters:
                sensored += letter
            else:
                sensored += '-'
        return sensored
    
    def getEntryMessage(self):
        return f"---HANGMAN!---\nSpace Edition\n\nGuess the space themed word by guessing letters, or enter the whole word if you think you know it!\n\n{self.getSensoredWord()}\n{self.getHangmanPicture()}"
    
    def getOutput(self):
        if self.getWrongGuessCount() == 6:
            return (True, f"{self.word}\n{self.getHangmanPicture()}\n\nYou Lost!")
        if self.checkForWin():
            return (True, f"{self.getSensoredWord()}\n{self.getHangmanPicture()}\n\nYou Win!")
        return (False, f"WORD: {self.getSensoredWord()}\nGuesses: {', '.join(self.letters)}\n{self.getHangmanPicture()}")
    
    def getHangmanPicture(self):
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
        return HANGMAN_PICS[self.getWrongGuessCount()]
    
    def getWrongGuessCount(self):
        return len(list(set(self.letters) - set(self.wordLetters)))