# Tic-Tac-Toe
Tic-Tac-Toe game implemented in Python using Object-Oriented Programming (OOP) principles for a structured and efficient approach.


## Class Descriptions

This section provides a breakdown of the key classes used in the Tic-Tac-Toe game:

**Player:**

- **Attributes:**
    - `name` (string): Stores the player's name.
    - `symbol` (character): Represents the player's symbol on the board (e.g., 'X' or 'O').
- **Methods:**
    - `choose_name()`: Prompts the player to enter their name and assigns it to the `name` attribute.
    - `choose_symbol()`: Allows the player to select their symbol and assigns it to the `symbol` attribute.

**Board:**

- **Attributes:**
    - `board` (2D list or array): Represents the game board state. Each element can be empty (' '), 'X', or 'O' depending on the player's move.
- **Methods:**
    - `display_board()`: Displays the current board state in a user-friendly format.
    - `update_board(row, col, symbol)`: Updates the board state at the specified row and column with the given player's symbol.
    - `reset_board()`: Clears the board state by setting all elements in the `board` attribute to empty.

**Menu:**

- **Attributes:** (This class likely doesn't have any attributes as you mentioned)
- **Methods:**
    - `display_main_menu()`: Presents the main menu options to the player (e.g., start new game, choose difficulty). This method might return the user's chosen option.
    - `display_endgame_menu()`: Displays options after the game ends (e.g., play again, quit). This method might also return the user's chosen option.

**Game:**

- **Attributes:**
    - `board`: An instance of the `Board` class, representing the game's board state.
    - `players`: A list containing instances of the `Player` class, representing the participating players.
    - `current_player_index` (integer): Tracks the current player's turn (index of the active player in the `players` list).
    - `menu`: An instance of the `Menu` class, used for player interaction through menus.
- **Methods:**
    - `start_game()`: Initializes the game by creating the board, assigning players, and potentially displaying starting information or instructions.
    - `player_turn()`: Manages a player's turn, including:
        - Displaying the board.
        - Prompting the player for their move and validating the input.
        - Updating the board state with the player's move.
        - Checking for win or draw conditions.
    - `check_win()`: Uses logic to determine if a player has achieved a winning condition on the board.
    - `check_draw()`: Checks if the board is full and no player has won, indicating a draw.
    - `restart_game()`: Resets the game by calling `board.reset_board()` and potentially other methods to prepare for a new game.
    - `quit_game()`: Ends the game and potentially displays a goodbye message or performs cleanup actions.

