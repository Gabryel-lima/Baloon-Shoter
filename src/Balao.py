import pygame
from pygame.locals import *

class Balao:
    def __init__(self, tela):
        self.tela = tela
        self.largura_balao_box = 50
        self.altura_balao_box = 50
        self.espaco_baloes_box = 10 
        self.num_colunas = 8
        self.num_blocos_por_fileira = 5
        self.posicao_box_x = 50
        self.posicao_box_y = 545
        self.balao_img = pygame.image.load('assets/images/balao.jpg')
        self.balao_img = pygame.transform.scale(self.balao_img, (self.largura_balao_box, self.altura_balao_box))
        self.baloes = [] 
        self.criar_baloes()
        self.box_baloes()

    def criar_baloes(self):
        for fileira in range(self.num_blocos_por_fileira):
            for coluna in range(self.num_colunas):
                self.x = self.posicao_box_x + coluna * (self.largura_balao_box + self.espaco_baloes_box)
                self.y = self.posicao_box_y - fileira * (self.altura_balao_box + self.espaco_baloes_box)
                balao = pygame.Rect(self.x, self.y, self.largura_balao_box, self.altura_balao_box)
                self.baloes.append(balao)
        return self.baloes
    
    def box_baloes(self):
        print(f"Tamanho da lista de coordenadas de balões: {len(self.baloes)}")
        for box in self.baloes:
            print(box)
    
    def desenhar_baloes(self):
        for balao in self.baloes:
            self.tela.blit(self.balao_img, balao)
