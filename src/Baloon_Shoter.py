
import json
import os

import cv2
import pygame
from pygame.locals import *

from Baloon_Shoter_Base import Baloon_Shoter_Base

class Baloon_Shoter(Baloon_Shoter_Base):
    def __init__(self):
        super().__init__()
        #self.icon = pygame.image.load('assets/logo.ico') #
        pygame.display.set_caption('Baloon-Shoter')
        #pygame.display.set_icon(self.icon) #
        #self.cap = cv2.VideoCapture('assets/videos/vfundo.mp4')
        self.pontos = 0
        #self.som_fim_nivel = pygame.mixer.Sound('')
        #self.fim_jogo = pygame.mixer.Sound('')
        #self.som_colisao = pygame.mixer.Sound('')
        self.relogio = pygame.time.Clock()
        self.mesg = f'Pontos: {self.pontos}'
        self.lp = self.carregar_melhor_pontuacao()
        self.mesg_bp = f'Melhor pontuação: {self.lp}' 
        self.fontei = pygame.font.SysFont('Candara', 30, True, False)
        self.jogo_iniciado = False

    def verifica_colissao(self):
        pass

    def som_da_bola_e_bloco(self):
        self.som = self.som_colisao
        self.som.set_volume(0.30)
        self.som.play()

    def som_de_fim_de_jogo(self):
        self.som = self.fim_jogo
        self.som.set_volume(0.30)
        self.som.play()

    def som_de_fim_de_nivel(self):
        self.som = self.som_fim_nivel
        self.som.set_volume(0.30)
        self.som.play()

    def carregar_melhor_pontuacao(self):
        try:
            with open('src/best_score.json', 'r') as file:
                data = json.load(file)
                return data['best_score']
        except (FileNotFoundError, KeyError):
            return 0

    def salvar_melhor_pontuacao(self):
        data = {'best_score': self.lp}
        with open('src/best_score.json', 'w') as file:
            json.dump(data, file)

    def atualiza_melhor_pontuacao(self):
        if self.pontos > self.lp:
            self.lp = self.pontos
            self.salvar_melhor_pontuacao()
            self.mesg_bp = f'Melhor pontuação: {self.lp}'

    def reset_melhor_pontuacao(self): # Não está sendo utilizado.
        self.lp = 0
        self.salvar_melhor_pontuacao()
        pass

    def atualiza_pontuacao(self):
        self.pontos += 1
        self.mesg = f'Pontos: {self.pontos}'

    def reset_pontos(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg = f'Pontos: {self.pontos}'
        else:
            self.pontos = 0
            self.mesg = f'Pontos: {self.pontos}'

    def reset_nivel(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg_nivel = f'Nivel: {self.nivel}'
        else:
            self.nivel = 1
            self.mesg_nivel = f'Nivel: {self.nivel}'

    def reset(self): # Esse metodo retorna o menu.
        self.jogo_iniciado = False

    def exibir_pontuacao(self):
        mensagem = self.mesg
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,430))

    def exibe_melhor_pontuacao(self):
        mensagem = self.mesg_bp
        texo_formatado = self.fontei.render(mensagem, False, (255,255,255))
        self.tela.blit(texo_formatado, (40,530))

    def exibir_nivel(self):
        mensagem = self.mesg_nivel
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,480))

    def mensagem_fim_de_nivel(self):
        if len(self.blocos.blocos) == 0:
            texto_formatado = self.fonte.render(f'Fim do Nivel {self.nivel}', False, (255,255,255))  
            self.tela.blit(texto_formatado, (self.altura // 2 - 100, self.largura // 2 - 80))
            self.niveis_count()
            self.som_de_fim_de_nivel()
            pygame.display.flip()
            pygame.time.delay(3000)
            self.blocos.resetar_blocos()
            self.bola.reset()
            self.continuar_prox_nivel()

    def layout(self):
        self.desenho_borda()
        self.botoes_tela_inicial_modos()
        self.selecao_de_modos_estrutura()
        self.balao.desenhar_baloes()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

            self.layout()
            self.relogio.tick(60)

        
            pygame.display.update()

if __name__ == '__main__':
    jogo = Baloon_Shoter()
    jogo.run()