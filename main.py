class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (a single letter)")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please choose a single letter.")


class Menu:
    def display_main_menu(self):
        print("Welcome to my Tic Tac Toe game!")
        print("1. Start Game")
        print("2. Quit Game")
        choice = input("Enter your choice (1 or 2): ")
        return choice

    def display_endgame_menu(self):
        menu_text = """
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2): """
        choice = input(menu_text)
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        # ["1", "2", "3", "4"..."9"]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("_"*5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for player in self.players:
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.board.display_board()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn ({current_player.symbol})")
            choice = int(input("Enter your move (1-9): "))
            if self.board.update_board(choice, current_player.symbol):
                if self.check_win(current_player.symbol):
                    self.board.display_board()
                    print(f"Congratulations! {current_player.name} wins!")
                    break
                elif self.check_draw():
                    self.board.display_board()
                    print("It's a draw!")
                    break
                self.switch_players()
            else:
                print("Invalid move. Try again.")

    def check_win(self, symbol):
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
            [1, 5, 9], [3, 5, 7]              # Diagonal
        ]
        for combo in winning_combinations:
            if all(self.board.board[pos - 1] == symbol for pos in combo):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def switch_players(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def quit_game(self):
        print("Thanks for playing!")
        exit()


game = Game()
game.start_game()
