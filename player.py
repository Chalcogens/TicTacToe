import math
import random
import time

class Player:
    def __init__(self, letter):  #init is a constructor
        self.letter = letter    #letter = "x" or "o"

    def get_move(self,game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter) #calls parent class (Player) init method

    def get_move(self,game):
        square = random.choice(game.available_moves())
        time.sleep(1)
        return square


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + "'s turn. Input move 0-8:")
            # input is valid only if it is an available integer from 0-8
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("invalid square. try again.")
        return val

class SmartComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves)
        else:
            square = self.minimax(game,self.letter)["position"] #choose best move based on minimax
        return square

    def minimax(self, game, player):
        player_to_maximise = self.letter
        player_to_minimise = "O" if player == "X" else "X"

        #first, we want to check if the previous move was a winner
        #this is our base case
        if game.current_winner == player_to_minimise:
            return{"position": None, "score": 1 * (game.num_empty_squares() + 1) if player_to_maximise == player_to_minimise else -1 * (game.num_empty_squares() + 1) }
        elif not game.empty_squares():
            return{"position": None, "score": 0}


        if player == player_to_maximise:
            best = {"position": None, "score": -math.inf} #each score should be maximised
        else:
            best = {"position": None, "score": math.inf}  # each score should be minimised

        for move in game.available_moves():
            #1: make the move
            game.make_move(move, player)
            #2: recurse using minmax to simulate a game after that move
            sim_score = self.minimax(game, player_to_minimise) #alternate players
            #3: undo the move
            game.board[move] = " "
            game.current_winner = None
            sim_score["position"] = move
            #4 update dictionaries with new scores if necessary
            if player == player_to_maximise: #maximise one player
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else: #minimise the other player
                if sim_score["score"] < best["score"]:
                    best = sim_score

        return best
