from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range (9)]  #single list to represent 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod # use static method here as it's not bound to an object (board)
    def print_board_nums(): # this function tells us which number corresponds to which box
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range (3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for (i,spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves

    def empty_squares(self):
        if ' ' in self.board:
            return True
        else:
            return False

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self,square,letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        #check row
        row_ind = square//3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #check diagonal. Note that the diagonal cells are even-indexed
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        #if all fail
        return False


def play(game, x_player, o_player, print_game):
    if print_game:
        game.print_board_nums()

    letter = "X" # by convention, X is the starting letter
    # iterate while game still has empty squares. Break out of loop when winner is returned
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print(" ")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"

    if print_game:
        print("It's a tie")

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = SmartComputerPlayer("O")
    t = TicTacToe()
    play(t,x_player, o_player, print_game=True)




