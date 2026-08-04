
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that practices string handling, loops, conditionals, and user interaction.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create a game setup that randomly selects a word from a predefined list and prepares the display used for player guesses.

#### Requirements
Completed program should:

- Define a list of possible secret words.
- Randomly choose one word for each new game.
- Initialize a display that hides unrevealed letters with underscores.
- Explain the rules and number of attempts to the player.

### 🛠️ Letter Guessing and Progress Display

#### Description
Implement user input to accept letter guesses and update the displayed progress for the hidden word.

#### Requirements
Completed program should:

- Ask the player to guess a letter each turn.
- Reveal correct letters in the hidden word display.
- Keep and show the current progress in `_ _ _` format.
- Prevent duplicate guesses from counting against the player.

### 🛠️ Win/Lose Conditions

#### Description
Track incorrect guesses and determine when the player wins or loses the game.

#### Requirements
Completed program should:

- Track how many incorrect guesses remain.
- End the game when the word is fully guessed or attempts run out.
- Display a win message if the player guesses the word.
- Display a lose message if the player runs out of attempts.
