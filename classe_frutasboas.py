import pygame as pg 
import random 



class Frutaboa:
    def __init__(self, endereco_imagem):
        self.frutaboa = pg.image.load(endereco_imagem)
        self.frutaboa = pg.transform.scale(self.frutaboa, (50,50))
        self.pos_x_frutaboa = random.randint(150,940)
        
        #criando um atributo
        self.pos_y_frutaboa = -10
        self.velocidade = random.randint (5,10)
        self.mascara = pg.mask.from_surface(self.frutaboa)
    
    def andar (self):
        self.pos_y_frutaboa = self.pos_y_frutaboa + self.velocidade

        if self.pos_y_frutaboa>800:
            self.voltar()
    
    def exibir(self, fundo):
        fundo.blit(self.frutaboa, (self.pos_x_frutaboa,self.pos_y_frutaboa))

    def voltar(self):
        self.pos_x_frutaboa = random.randint(150,940)
        self.pos_y_frutaboa = -100
        
        self.velocidade = random.randint(5,10) 

