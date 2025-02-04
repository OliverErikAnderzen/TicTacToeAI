class Model:
    def __init__(self, data):
        self.cell_size = data["cell_size"]
        self.grid_size = data["grid_size"]
        self.game_over = False

    def set_game_over(self, new_status):
        if new_status == True or new_status == False:
            self.game_over = new_status
