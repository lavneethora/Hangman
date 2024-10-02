# Hangman Game

## Overview

The **Hangman Game** is a Python-based console application that allows users to play the classic word-guessing game. Players try to guess a hidden word by suggesting letters, one at a time, within a limited number of attempts. The game is designed for single-player use and can handle a variety of words from a predefined list or a file.

## Key Features

- **Word Guessing:** Players attempt to guess a hidden word, one letter at a time.
- **Limited Guesses:** Players have a finite number of wrong guesses before the game is over.
- **Random Word Selection:** The game randomly selects words from a predefined list.
- **Real-time Feedback:** The game provides real-time feedback on the guessed letters, showing correct and incorrect guesses.
- **Game Over Scenarios:** The game ends either when the word is correctly guessed or when the player runs out of attempts.
  
## How to Play

1. **Start the Game:** Launch the Python program in the terminal.
2. **Guess a Letter:** The program will display the hidden word as underscores (_), and you can guess one letter at a time.
3. **View Progress:** Each correct guess will reveal the corresponding letter(s) in the word. Incorrect guesses reduce the number of remaining attempts.
4. **Winning:** Guess all the letters in the word correctly before running out of attempts to win the game.
5. **Losing:** If you run out of attempts before guessing the word, the game will reveal the correct word and end.

## Example

```bash
_ _ _ _ _ 
Guess a letter: e
e _ _ _ _ 
Guess a letter: a
e _ _ a _ 
Guess a letter: r
e _ r a _ 
Congratulations, you guessed the word "erase"!
```

## Installation and Running

1. **Clone the Repository**:
```bash
git clone https://github.com/lavneethora/Hangman.git
```

2. **Navigate to the Project Directory**:
```bash
cd Hangman
```

3. **Run the Game**:
```bash
python hangman.py
```

## Game Flow

- **Random Word Selection**: A word is randomly selected from the predefined list or file.
- **Input Validation**: Ensures that the player enters valid alphabetic characters.
- **Attempt Tracking**: Tracks the number of incorrect guesses and displays remaining attempts.
- **Word Display**: Continuously updates the display of the word with correctly guessed letters.
- **Game Over Condition**: The game ends when the player either guesses the word or runs out of attempts.

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
- Feel free to submit issues or pull requests for any improvements or bug fixes.

## Author

- Lavneet Hora
- Sophomore @ Texas Tech University
- Computer Science
