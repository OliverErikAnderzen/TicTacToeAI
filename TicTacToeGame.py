from Model import Model
from View import View
from Controller import Controller

import pygame

def TicTacToeGame():
    data = {
        "grid_size": (3,3),
        "cell_size": 40
    }

    pygame.init()

    #initialize model
    model = Model(data)

    #initialize view
    view = View(model)

    #initialize controller
    controller = Controller(model, view)

    controller.run()

if __name__ == "__main__":
    TicTacToeGame()