import random
from lists import word_list
from art import hangman_logo
from art import stages

game_end = False
chosen_word = random.choice(word_list)
lives = 6
print(hangman_logo)

display = []
for letter in chosen_word:
    letter = "_"        
    display.append(letter)

chosen_word_list = []
for letter in chosen_word:
    chosen_word_list.append(letter)
    
while game_end == False:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
            print("You've already guessed " ,guess)

    for position in range(len(chosen_word)):
        if guess == chosen_word_list[position]:
            display[position] = guess
      
    if guess not in chosen_word:
        print("You guessed " ,guess , "that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_end = True
            print("The word was ", chosen_word)
            print("You lose!!")
            
    print(f"{' '.join(display)}")
        
    if "_" not in display:
        game_end = "True"
        print("You Win!!")
        
    print(stages[lives])