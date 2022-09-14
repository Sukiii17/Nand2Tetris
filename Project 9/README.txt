My game:
I wrote a Tic Tac Toe in jack where the computer is supposed to play wisely against human. The detailed rules of the game are too well-known to be explained here, but I have included an instruction in the game that can be viewed when running the program.

The folder contains the following items:
- Folder TicTacToe: Contains all files needed to run in the VMEmulator:
  - Board.jack: this file deals with the graphic presentation, such as drawing the board, noughts, crosses, etc.
  - BoardGame.jack: main meat of the program, where an algorithm on how computer plays against human is included. Also the whole game is programmed in this file.
  - Main.jack
- A demonstration of me running the program in the VMEmulator.
- A Python program that does the same (it is just a quick piece I wrote before for conceptual debugging and logic purpose).

The algorithm:
The AI part of the program goes as follows:
The computer consider doing the following in order:
- If there is an available position that can prevent the player from winning or the computer can win, it will move there.
- If there is available corner cells, it will randomly pick one and move there.
- If the center is available, it will move there.
- If all the above is not available, it will randomly pick an edge option and move there.

What worked?
- The program runs and can basically do what is supposed to do.
- There is an instruction at the beginning of the game.
- There is an AI part of the piece.
- There is drawing and graphical demonstration of the game, which uses screen and keyboard.

What didn't work?
- The program is still not bug free.
- For the AI part, when I try to play the game multiple times, I think the computer does not always play optimally, as it is programmed to do. Also, the random function seems to be investigated, as it does not always play randomly in some cases where it should. This indicates there should be bug somewhere undiscovered.
- For some parts of the showing on the screen, it should be improved.
- I only include one round of the game. For a better development, one can design a button to press to continue for a second round of game.


Note: Sorry, I was too occupied by my other courses this week and is late for the project. Also, this project still has some parts that I should improve and debug.