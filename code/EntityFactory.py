import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Destroyers import Destroyers
from code.Player import Player


class EntityFactory:

    @staticmethod
    def obtain_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []
                for i in range(3):  # level2Bg images number
                    lista_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    lista_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return lista_bg
            case 'Level2Bg':
                lista_bg = []
                for i in range(3):  # level2Bg images number
                    lista_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    lista_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return lista_bg
            case 'Player':
                return Player('Player', (50, WIN_HEIGHT / 2))
            case 'Meteor1':
                return Destroyers('Meteor1', (WIN_WIDTH, random.randint(40, WIN_HEIGHT - 40)))
            case 'Meteor2':
                return Destroyers('Meteor2', (WIN_WIDTH + 5, random.randint(40, WIN_HEIGHT - 40)))
            case 'Missile1':
                return Destroyers('Missile1', (WIN_WIDTH, random.randint(40, WIN_HEIGHT - 40)))
            case 'Missile2':
                return Destroyers('Missile2', (WIN_WIDTH + 5, random.randint(40, WIN_HEIGHT - 40)))
