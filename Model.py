class Model:
    def __init__(self, data):
        self.cell_size = data["cell_size"]
        self.grid_size = data["grid_size"]
        self.game_over = False
        self.turn = 'O'

    def set_game_over(self, new_status):
        if new_status == True or new_status == False:
            self.game_over = new_status

    def change_turn(self):
        if self.turn == 'O':
            self.turn = 'X'
        else:
            self.turn = 'O'

    def handle_action(self, action):
        position = action.pos
        self.place_piece(position)
        self.change_turn()

    def place_piece(self, position):
