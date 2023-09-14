

import pygame
from pygame.locals import *

from Player_Base import PlayerBase

class Player(PlayerBase):
    def __init__(self, tela, borda, raio, largura, altura):
        super().__init__(tela, borda, raio, largura, altura)

    def desenho_player(self):
        pygame.mouse.set_visible(False)
        cor = (255,0,0)
        self.x, self.y = pygame.mouse.get_pos()
        self.tela.fill((0,0,0))
        centro = (int(self.x), int(self.y))
        pygame.draw.circle(self.tela, cor, centro, int(self.raio), width=3)
        pygame.draw.line(self.tela, cor, (centro[0] - self.raio, centro[1]), (centro[0] + self.raio, centro[1]), width=1)
        pygame.draw.line(self.tela, cor, (centro[0], centro[1] - self.raio), (centro[0], centro[1] + self.raio), width=1)

    def input_player(self):
        pass

    def resetp(self):
        pass