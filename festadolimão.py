#importano o py game
import pygame as pg 
#colocando o resource para converter em exe depois
from caminho_relativo import resource_path as rp
#adicionando a limaozinho
from classe_jogador import Jogador

pg.init() #inicializa os módulos do pygame, a maioria iria funcionar sem, mas alguns necessitam inicializar

clock = pg.time.Clock()

#Criando a tela
tela = pg.display.set_mode((1000,700))

#configurando a tela
pg.display.set_caption ("FESTA DO LIMÃO")

#carregando as imagens 
fundo = pg.image.load(rp("scr/img/fundo.png"))
como_jogar = pg.image.load(rp("scr/img/comojogar.png"))
limaozinho = pg.image.load(rp("scr/img/limãozinho.png"))
capa_inicio = pg.image.load(rp("scr/img/capadeinicio.png"))
capa_perdeu = pg.image.load(rp("scr/img/capaperdeu.png"))
capa_ganhou = pg.image.load(rp("scr/img/capaganhou.png"))

#ajustando a imagem
fundo = pg.transform.scale (fundo, (1000,700))
como_jogar = pg.transform.scale (como_jogar, (1000,700))
capa_perdeu = pg.transform.scale (capa_perdeu, (1000,700))
capa_ganhou = pg.transform.scale (capa_ganhou, (1000,700))
capa_inicio = pg.transform.scale (capa_inicio, (1000,700))

status_jogo = "INICIO"
limaozinho = Jogador()
# --- LOOP PRINCIPAL DO JOGO ---
rodando = True
while rodando:
    # 1. Controla a taxa de quadros (FPS)
    clock.tick(60)

    # 2. Verifica se o usuário quer fechar o jogo
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

    #tela de inicio
    teclas_pressionadas = pg.key.get_pressed()
    if status_jogo == "INICIO":
        tela.blit(capa_inicio, (0, 0))
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "TUTORIAL"
    if status_jogo == "TUTORIAL":
         tela.blit(como_jogar, (0, 0))
         if teclas_pressionadas [pg.K_UP]:
             status_jogo = "JOGANDO"
    
    if status_jogo == "JOGANDO":
        tela.blit(fundo, (0,0))
        limaozinho.exibir(tela)
        limaozinho.andar(teclas_pressionadas)


 
    

    # 4. Atualiza a tela para mostrar os desenhos novos
    pg.display.update()





