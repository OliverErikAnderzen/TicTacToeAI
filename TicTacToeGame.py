from Model import Model
from View import View
from Controller import Controller

import pygame

def TicTacToeGame():
    data = {
        "grid_size": 40,
        "cell_size": (3,3)
    }

    pygame.init()

    #initialize model
    model = Model(data)

    #initialize view
    view = View(Model)

    #initialize controller
    controller = Controller(Model, View)

if __name__ == "__main__":
    TicTacToeGame()