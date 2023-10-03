import time

word = 'house'
word_index = []

word_spaces = []
for i in word:
    word_spaces.append("_")

for i in word:
    word_index.append(i)

def startup():
    print("Welcome to HANGMAN!")
    time.sleep(2)
    print("Try to guess the word by guessing letters. You get 10 guesses.")
    time.sleep(2)
    print("Good Luck!")

def letter_guesses():
    guesses = []
    numberOfGuesses = 10
    while numberOfGuesses > 0:
        print(* word_spaces)
        user_guess = input("Guess a letter: ")
        if numberOfGuesses == 1:
            guesses.append(user_guess.lower())
            print(*guesses)
            print("The correct answer was "+ word +".")
            print("Game Over. Good-bye!")
            break
        elif not str(user_guess).isalpha():
            print("Please guess a letter.")
        elif str(user_guess).isalpha() and user_guess.lower() not in guesses:
            indices = [i for i, x in enumerate(word_index) if x == user_guess.lower()]
            for i in indices:
                word_spaces[i]=user_guess.lower()
            guesses.append(user_guess.lower())
            numberOfGuesses = numberOfGuesses-1
            print("you have "+str(numberOfGuesses)+" left.")
            print(*guesses)
            
            if word_spaces == word_index:
                print("You guessed the correct word, "+word+"!")
                print("Congrats, you WON!!!!")
                break

        elif str(user_guess).isalpha() and user_guess.lower() in guesses :
            print("You already guessed that letter. Please try again")


startup()
letter_guesses()