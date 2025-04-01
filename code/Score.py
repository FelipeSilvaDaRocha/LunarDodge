import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE
from pygame.font import Font

from code.Const import COLOR_WHITE, SCORE_POS
from code.ProxyDB import ProxyDB


def formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f'{current_time} - {current_date}'


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect()

    def save(self,):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)  # Parameter -1 is used to loop the music
        db_proxy = ProxyDB('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.text_score(48, 'GAME OVER!', COLOR_WHITE, SCORE_POS['TitleText'])
            score = None
            msg = 'Enter Player name: (6 - characters)'
            self.text_score(20, msg, COLOR_WHITE, SCORE_POS['MsgName'])
            self.text_score(40, 'DEMO', COLOR_WHITE, SCORE_POS['Name'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()

    def show(self, ):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)  # Parameter -1 is used to loop the music
        self.window.blit(source=self.surf, dest=self.rect)
        self.text_score(48, 'SCORE', COLOR_WHITE, SCORE_POS['TitleText'])
        self.text_score(20, ' NAME          SCORE                   DATE         ', COLOR_WHITE, SCORE_POS['Label'])
        self.text_score(40, 'DEMO', COLOR_WHITE, SCORE_POS['Name'])
        banco_proxy = ProxyDB('DBScore')
        list_score = banco_proxy.retrieve()
        banco_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.text_score(20, f'{name}     {score :05d}     {date}', COLOR_WHITE,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    sys.exit()  # end pygame
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()  # Close window
                        sys.exit()  # end pygame
            pygame.display.flip()

    def text_score(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
