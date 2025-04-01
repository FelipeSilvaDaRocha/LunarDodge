import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 242, 0)

#  E
EVENT_METEOR = pygame.USEREVENT + 1
EVENT_DEST = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 0,
    'Level1Bg2': 3,
    'Level2Bg0': 1,
    'Level2Bg1': 0,
    'Level2Bg2': 3,
    'Player': 10,
    'Meteor1': 20,
    'Meteor2': 9,
    'Missile1': 9,
    'Missile2': 15
}
#  M
MENU_OPTION = ('START NOW',
               'SCORE',
               'EXIT')

#  T
TIME_DEST = 100  # 1 second
TIME_METEOR = 1000

#  W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'TitleText': (WIN_WIDTH / 2, 50),
             'MsgName': (WIN_WIDTH / 2, 90),
             'Label': (WIN_WIDTH / 2, 100),
             'Name': (WIN_WIDTH / 2, 160)
             }
