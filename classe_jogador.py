import pygame as pg 
import random 
from caminho_relativo import resource_path as rp

class Jogador:
    def __init__(self):

        self.imagem = pg.image.load(rp("scr/img/limãozinho.png"))
        self.imagem = limaozinho = pg.transform.scale(self.imagem, (100, 150))

        self.pos_x = 0
        self.pos_y = 700-150
        self.mascara = pg.mask.from_surface (self.imagem)
        self.velocidade = 10
        self.correndo = False          
        self.tempo_inicio_corrida = 0  
        self.usos_corrida = 0          
        self.limite_usos = 3
        self.somruim = pg.mixer.Sound(rp("scr/sound/ponstosruins.mp3"))
        self.sombom = pg.mixer.Sound (rp("scr/sound/pontosbom.mp3"))
        self.somperdeu = pg.mixer.Sound (rp("scr/sound/sompedeu.mp3"))
        self.somganhou = pg.mixer.Sound (rp("scr/sound/somganhou.mp3"))

    def andar(self, teclas_pressionadas):
        # tempo atual do jogo em milissegundos
        tempo_atual = pg.time.get_ticks()
        
        # 2. Se o jogador já estiver correndo, checa se os 5 segundos (5000 ms) acabaram
        if self.correndo:
            if tempo_atual - self.tempo_inicio_corrida > 5000:
                self.correndo = False # Acabou o tempo, volta ao normal
    

        # 3. Se o jogador apertar ESPAÇO, NÃO estiver correndo e ainda tiver usos disponíveis:
        if teclas_pressionadas[pg.K_SPACE] and not self.correndo and self.usos_corrida < self.limite_usos:
            self.correndo = True
            self.tempo_inicio_corrida = tempo_atual # Salva quando começou
            self.usos_corrida += 1                  # Gasta um uso
           

        # 4. Define a velocidade com base no estado da corrida
        if self.correndo:
            velocidade_atual = 20  # Velocidade rápida
        else:
            velocidade_atual = self.velocidade  # Velocidade padrão (10)

        # 5. Movimentação normal da sua personagem usando a 'velocidade_atual'
        if teclas_pressionadas[pg.K_RIGHT]:
            if self.pos_x < 1000 - self.imagem.get_width():
                self.pos_x = self.pos_x + velocidade_atual

        if teclas_pressionadas[pg.K_LEFT]:
            if self.pos_x > 0:
                self.pos_x = self.pos_x - velocidade_atual
        
    

    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x,self.pos_y))
        self.mascara = pg.mask.from_surface(self.imagem)
    
    def voltar(self):
        self.pos_x = 0
        self.pos_y = 700-150
    
    def ruim(self):
        self.somruim.play()

    def bom(self):
        self.sombom.play()

    def perdeu(self):
        self.somperdeu.play()

    def ganhou (self):
        self.somganhou.play()
