# hangman
### terminal based hangman game

Hello, this is a simple text-based hangman game that you can run from your terminal!

###To play the game:
- Save the hangman.py file
- Run the file from your terminal using python3 (e.g. "python3 hangman.py")
- Play the game and have fun!

###What this project does:

Functions
- setup function, defines a list of words and randomly selects one for the game
- clear function, clears the terminal window to reduce clutter
- hang function, prints ASCII art for the hangman visual
- victory functiom, prints different messages depending on if the user wins or loses

 Main function
 - Loops the game until either the win condition is true or the user uses all 7 attempts
 - Validates inputs for length, being an alphabet, and not already being guessed (attempts are not used unless the input is valid)
 - Incorrect guesses reduce number of attempts, prints message, and prints hangman with another piece
 - Correct guesses print message, print hangman, adds letter guessed to list of correct letters
 - Each loop prints the blank spaces, with any letters correctly guessed filled in, and a list of all the letters already guessed
 - Calls victory function which prints message dependent on win condition being True or False

To add in future:
- choosing categories: sports, genres, animals, etc.
