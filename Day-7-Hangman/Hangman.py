import random
from Hangman_words import wordList
from Hangman_art import stages, logo

print(logo)
chosenWord = random.choice(wordList)
display = []
turns = True
lives = 6

#Test code
#print(f"psst, the chosen word is {chosenWord}")

for i in range(len(chosenWord)):
    display.append('_')
print(display)

while turns:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed '{guess.upper()}', try another letter.")
    for i in range(len(chosenWord)):
        if chosenWord[i] == guess:
            display[i] = guess
    print(display)
    
    
    if guess not in chosenWord:
        lives -= 1
        print(f"The letter '{guess.upper()}' is not in the chosen word. You have {lives} lives left.")
        if lives == 0:
            turns = False
            print(f'You lose')
            print(f"The correct word is {chosenWord}")

    
    if '_' not in display:
        turns = False
        print("You win!")
    
    print(stages[lives])
    