class Model:
    def __init__(self, data):
        self.cell_size = data["cell_size"]
        self.grid_size = data["grid_size"]
        self.game_over = False
        self.turn = 'O'
        self.game_representation = [
            [None, None, None],[None, None, None],[None, None, None]]

    def set_game_over(self, new_status):
        if new_status == True or new_status == False:
            self.game_over = new_status

    def get_game_over(self):
        return self.game_over
    
    def check_game_over(self):
        if self.check_win():
            self.set_game_over(True)

    def change_turn(self):
        if self.turn == 'O':
            self.turn = 'X'
        else:
            self.turn = 'O'

    def handle_action(self, action):
        position = action.pos
        self.place_piece(position)
        self.change_turn()

    def find_axis_square(self, axis_position):
        if axis_position < self.cell_size:
            return 0
        elif axis_position < self.cell_size * 2:
            return 1
        else:
            return 2

    def place_piece(self, position):
        square_position = (self.find_axis_square(position[1]), self.find_axis_square(position[0]))
        self.game_representation[square_position[0]][square_position[1]] = self.turn

    def check_diagonal_win(self):
        rep = self.game_representation
        if rep[0][0] == rep[1][1] and rep[1][1] == rep[2][2] and rep[1][1] != None:
            return True
        elif rep[0][2] == rep[1][1] and rep[1][1] == rep[2][0] and rep[1][1] != None:
            return True
        return False

    def check_horizontal_win(self):
        rep = self.game_representation

        for i in range(3):
            if rep[i][0] == rep[i][1] and rep[i][1] == rep[i][2] and rep[i][1] != None:
                return True
        return False
    
    def check_vertical_win(self):
        rep = self.game_representation

        for i in range(3):
            if rep[0][i] == rep[1][i] and rep[1][i] == rep[2][i] and rep[1][i] != None:
                return True
        return False

    def check_win(self):
        return self.check_diagonal_win() or self.check_vertical_win() or self.check_horizontal_win()
        