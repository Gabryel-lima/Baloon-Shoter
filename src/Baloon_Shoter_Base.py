
import json
import os
import webbrowser

import pygame
from pygame.locals import *

from Player import Player
from Balao import Balao


class Baloon_Shoter_Base:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.raio = 25
        self.fonte = pygame.font.SysFont('arial', 35, True, False)
        self.clink_rect = pygame.Rect(40,522,280,30)
        self.player = Player(self.tela, self.borda, self.raio, self.largura, self.altura)
        self.balao = Balao(self.tela)
        self.modo = f'Jogar'
        self.fonte_impact = pygame.font.SysFont("impact", 28)
        self.cor_botao_subl = (250,250,250)
        self.rect_botao_player = pygame.Rect(240,170,120,40)
        self.rect_botao_voltar = pygame.Rect(40,300,85,30)
        self.back = f'Voltar'
        self.mesgite = f'Pressione a tecla "Enter" para iniciar'
        self.nivel = 1
        self.mesg_nivel = f'Nivel: {self.nivel}'

    def desenho_borda(self):
        pygame.draw.rect(self.tela, (115,115,115), self.borda, width=3)

    def exibir_mensagem_inte_iniciar(self):
        mensagem = self.mesgite
        fonte = pygame.font.SysFont('times new roman', 25, True, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (100,205))
        mensagem = self.mesgc
        fonte = pygame.font.SysFont('colibri', 30, False, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (60,240))

    def botoes_tela_inicial_modos(self):
        pos_mouse = pygame.mouse.get_pos()
        mod = self.modo
        rect_modo = self.rect_botao_player

        if rect_modo.collidepoint(pos_mouse):
            self.cor_botao_modo = (170,170,170)
        else:
            self.cor_botao_modo = (255,255,255)
        
        if self.rect_botao_player.width > 0 and self.clink_rect.width > 0:
            texto_formatado = self.fonte.render(mod, False, self.cor_botao_modo)
            self.tela.blit(texto_formatado, (260,180))

    def exibir_credito(self):
        mensagem = self.credito
        texto_formatado = self.fonte_impact.render(mensagem, False, (255,255,255))
        self.tela.blit(texto_formatado, (40,520))

    def desenho_botao_back(self):
        pos_mouse = pygame.mouse.get_pos()
        rect_botao = self.rect_botao_voltar
        mensagem = self.back

        if rect_botao.collidepoint(pos_mouse):
            self.cor_botao_voltar = (150,150,150)
            self.cor_botao_subl = (200,200,200)
        else:
            self.cor_botao_voltar = (255,255,255)
            self.cor_botao_subl = (200,200,200)

        if self.rect_botao_voltar.width > 0:  
            texto_formatado = self.fonte.render(mensagem, False, self.cor_botao_voltar)
            self.tela.blit(texto_formatado, (40,300))

        return rect_botao
    
    def selecao_de_modos_estrutura(self): #Tela de menu.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                
                if self.rect_botao_player.collidepoint(pos_mouse):
                    self.rect_botao_player = pygame.Rect(0,0,0,0)
                    pygame.time.delay(300)
                    self.modo_jogador = "Jogar"

                    self.executar_particao(self.selecao_de_modos_estrutura_particao)

                elif self.clink_rect.collidepoint(event.pos):
                        webbrowser.open("https://github.com/Gabryel-lima")
                        pygame.time.delay(300)

    def executar_particao(self, particao): #Antes do inicio do jogo.
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        os._exit(0)

                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if self.desenho_botao_back().collidepoint(pygame.mouse.get_pos()):
                            self.reset()
                            pygame.time.delay(300)
                            return
                        
                    if event.type == KEYDOWN and event.key == K_RETURN:
                        self.jogo_iniciado = True
                        #self.bola.iniciar_movimento() #Substituir por desenho do Rect dos balões.
                        if self.modo_jogador == "Jogar":
                            self.player.reset()
                            return
                    else:
                        self.tela.fill((0,0,0))
                        self.desenho_botao_back()
                        self.desenho_borda()
                        #self.bola.desenho_bola() #Substituir por desenho do Rect dos balões.
                        self.exibir_mensagem_inte_iniciar()
                        particao()
                        pygame.display.update()

    def selecao_de_modos_estrutura_particao(self):
        self.player.desenho_player()

    def niveis_count(self):
        self.nivel += 1
        self.mesg_nivel = f'Nivel: {self.nivel}'

    def manipula_nivel(self):
        pass
        while True:
            self.blocos.configurar_nivel()
            break

    def continuar_prox_nivel(self):
        pass
        self.jogo_iniciado = True
        self.bola.iniciar_movimento()
        #self.manipula_nivel()
        self.rect_botao_player = pygame.Rect(0,0,0,0)
        return