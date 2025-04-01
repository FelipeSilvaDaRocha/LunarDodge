import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_METEOR, EVENT_DEST, TIME_DEST, TIME_METEOR
from code.Destroyers import Destroyers
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Score import Score


class Level:
    def __init__(self, window: Surface, name: str, score_player: list[int]):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.obtain_entity(self.name + 'Bg'))
        player = EntityFactory.obtain_entity('Player')
        player.score = score_player
        self.entity_list.append(player)
        self.score = 0
        pygame.time.set_timer(EVENT_METEOR, TIME_METEOR)
        pygame.time.set_timer(EVENT_DEST, TIME_DEST)

    def run(self, ):
        score = Score(self.window)
        pygame.mixer_music.load('./asset/Level.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            for enti in self.entity_list:
                self.window.blit(source=enti.surf, dest=enti.rect)
                enti.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_METEOR:
                    if self.name == 'Level1':
                        choice = random.choice(('Missile1', 'Missile2'))
                        self.entity_list.append(EntityFactory.obtain_entity(choice))
                    if self.name == 'Level2':
                        choice = random.choice(('Meteor1', 'Meteor2'))
                        self.entity_list.append(EntityFactory.obtain_entity(choice))
                if event.type == EVENT_DEST:
                    self.score += 1
                    if self.score == 100:
                        if self.name == 'Level1' or 'Level2':
                            return True
                        else:
                            score.save()

            self.text_level(15, f'Score: {self.score}', COLOR_WHITE, (50, 10))
            self.text_level(15, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (40, 30))
            self.text_level(15, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (50, WIN_HEIGHT - 20))
            pygame.display.flip()

            gameObver = EntityMediator.verify_collision(entity_list=self.entity_list)
            if gameObver:
                score.save()

    def text_level(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
