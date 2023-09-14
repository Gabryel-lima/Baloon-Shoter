

import pygame
from pygame.locals import *


class PlayerBase:
    def __init__(self, tela, borda, raio, largura, altura, x=300, y=300):
        self.tela = tela
        self.borda = borda
        self.colisao = borda
        self.raio = raio
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y
