import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        score = Score(self.window)
        menu = Menu(self.window)
        menu_return = menu.run()

        while True:
            if menu_return == MENU_OPTION[0]:
                score_player = []
                level = Level(self.window, 'Level1', score_player)
                level_return = level.run()
                if level_return:
                    level = Level(self.window, 'Level2', score_player)
                    level_return = level.run()
                    if level_return:
                        score.save()
            elif menu_return == MENU_OPTION[1]:
                score.show()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()
            else:
                pass

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
