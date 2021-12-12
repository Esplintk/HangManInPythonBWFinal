import random
from collections import defaultdict
import string
from listOfWords import randomWords

#Reviews of the games, the players can leave.
class Review:
    def __init__(self, theReview):
        self.theReview = theReview

class Hint:
    # Mapping Numeric values to the letters of the English Alphabet.
    def __init__(self, word):
        self.word = word


    def popularLetters(variable):
        letters = ['E', 'A', 'R', 'I', 'O', 'T', 'N', 'S', 'L', 'C']
        if (variable in letters):
            return True
        else:
            return False

    def filterOutPopLetters():
        seperatedWord = list(word)
        filteredWord = filter(popularLetters, seperatedWord)
        print("The popular letter(s) of this word are:")
        for s in filteredWord:
            print(s)



userReview = Review("")
popHint = Hint("")
#wordPoints = WordPointLevel()


def wordSelect():
    word = random.choice(randomWords)
    return word.upper()


def play(word):
    wordCompletion = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    lives = 6

    print("Welcome to my game of hangman!")
    print(showLives(lives))
    print(wordCompletion)
    print("\n")

    while not guessed and lives > 0:
        userGuess = input("Please guess a letter or a word: ").upper()
        if len(userGuess) == 1 and userGuess.isalpha():
            if userGuess in guessedLetters:
                print("You've already made that guess.", userGuess)
            elif userGuess not in word:
                print(userGuess, "is not present in the word.")
                lives -= 1
                guessedLetters.append(userGuess)
                print(showLives(lives))
                print(wordCompletion)
                answer = input("Would you like a hint of telling you all of the popular letters? (may be helpful may not be) (WARNING COSTS 2 LIVES) (Y/N)").upper()
                if "Y" in answer:
                    lives-=2
                    popHint.filterOutPopLetters
                    print(showLives(lives))
                    print(wordCompletion)
            else:
                print("Correct,", userGuess, "is in the word!")
                guessedLetters.append(userGuess)
                wordSeperated = list (wordCompletion)
                indicies = [i for i, letter in enumerate(word) if letter == userGuess]
                for index in indicies:
                    wordSeperated[index] = userGuess
                wordCompletion = "".join(wordSeperated)
                print(wordCompletion)

                if "_" not in wordCompletion:
                    guessed = True
        elif len(userGuess) == len(word) and userGuess.isalpha():
            if userGuess in guessedWords:
                print("The word has already been guessed", userGuess)
            elif userGuess != word:
                print(userGuess, "is not in the word.")
                lives -= 1
                guessedWords.append(userGuess)
                print(showLives(lives))
                print(wordCompletion)
            else:
                guessed = True
                wordCompletion = word
                print(wordCompletion)
        else:
            print("Not a valid guess.")
            print(showLives(lives))
            print(wordCompletion)
            print("\n")
        if guessed:
            print("Congratulations! You have guessed the word!")
        elif lives == 0:
            print("Sorry, you have died without guessing the word, Better luck next time.")
            print("The word was " + word)
        else:
            print("\n")


def showLives(lives):
    stages = [
        """
        -----------
        |         |
        |         O
        |        \\|/
        |         |
        |        / \\
        |
        |
   ----------------
        """,

        """
        -----------
        |         |
        |         O
        |        \\|/
        |         |
        |        / 
        |
        |
   ----------------
        """,

        """
        -----------
        |         |
        |         O
        |        \\|/
        |         |
        |        
        |
        |
   ----------------
        """,

        """
        -----------
        |         |
        |         O
        |        \\|
        |         |
        |        
        |
        |
   ----------------
        """,

        """
        -----------
        |         |
        |         O
        |         |
        |         |
        |        
        |
        |
   ----------------
        """,

        """
        -----------
        |         |
        |         O
        |         
        |         
        |        
        |
        |
   ----------------
        """,

        """
        -----------
        |         |
        |         
        |         
        |         
        |        
        |
        |
   ----------------
        """,
        ]
    return stages[lives]





def main():
    word = wordSelect()
    play(word)
    answer = input("Would you like to leave a review of the game? (Y/N)").upper()
    if "Y" in answer:
        response = input()
        userReview.theReview = response
    else:
        print("Thanks for playing my hangman")
    while input("Do you wish to play again? (Y/N)").upper() == "Y":
        word = wordSelect()
        play(word)



if __name__ == "__main__":
    main()