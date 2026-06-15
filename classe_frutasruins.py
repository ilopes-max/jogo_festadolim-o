import pygame as pg
import random

class Frutaruim:
    def __init__(self, endereco_imagem):
        self.frutaruim = pg.image.load(endereco_imagem)
        self.frutaruim = pg.transform.scale(self.frutaruim, (60,50))
        self.pos_x_frutaruim = random.randint(150,940)
        
        #criando um atributo
        self.pos_y_frutaruim = -10
        self.velocidade = random.randint (5,10)
        self.mascara = pg.mask.from_surface(self.frutaruim)
    
    def andar (self):
        self.pos_y_frutaruim = self.pos_y_frutaruim + self.velocidade

        if self.pos_y_frutaruim>800:
            self.voltar()
    
    def exibir(self, fundo):
        fundo.blit(self.frutaruim, (self.pos_x_frutaruim,self.pos_y_frutaruim))

    def voltar(self):
        self.pos_x_frutaruim = random.randint(150,940)
        self.pos_y_frutaruim = -100
        
        self.velocidade = random.randint(5,10) 