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
        print(position)
        square_position = (self.find_axis_square(position[1]), self.find_axis_square(position[0]))
        self.game_representation[square_position[0]][square_position[1]] = self.turn

