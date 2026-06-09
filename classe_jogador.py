import pygame as pg 
import random 
from caminho_relativo import resource_path as rp

class Jogador:
    def __int__(self):

        self.imagem = pg.image.load(rp("scr/img/limãozinho.png"))
        self.imagem = limaozinho = pg.transform.scale(self.imagem, (90, 90))

        self.pos_x = 0
        self.pos_y = 0
        self.mascara = pg.mask.from_surface (self.imagem)

        def andar (self, teclas_pressionadas):
            if teclas_pressionadas[pg.K_RIGHT]:
                if self.pos_y < 1000 - self.imagem.get_width():
                    self.pos_y = self.pos_y + 10
        
            if teclas_pressionadas[pg.K_LEFT]:
                if self.pos_y > 0:
                    self.pos_y = self.pos_y -10
        

    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x,self.pos_y))
        self.mascara = pg.mask.from_surface(self.imagem)
    
    def voltar(self):
        self.pos_x = 0
        self.pos_y = 0