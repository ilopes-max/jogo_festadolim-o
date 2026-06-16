#importano o pygame
import pygame as pg 
#colocando o resource para converter em exe depois
from caminho_relativo import resource_path as rp
#adicionando a limaozinho
from classe_jogador import Jogador
#adicionando fruta ruim
from classe_frutasruins import Frutaruim
#adicionando fruta boa
from classe_frutasboas import Frutaboa

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

#Criando frutas ruins
lista_frutaruim = [Frutaruim (rp("scr/img/ovoruim.png")),
                   Frutaruim (rp("scr/img/mosca.png")),
                   Frutaruim (rp("scr/img/limãoruim.png"))]

#criando frutas boas
lista_frutaboa = [Frutaboa (rp("scr/img/cupcakebom.png")),
                  Frutaboa (rp("scr/img/limãobom.png")),
                  Frutaboa (rp("scr/img/limonadaboa.png")),
                  Frutaboa (rp("scr/img/sorvetebom.png")),
                  Frutaboa (rp("scr/img/tortaboa.png"))]
#ajustando a fonte de pontuação
fonte = pg.font.SysFont("Elephant", 16,True,False)

status_jogo = "INICIO"
limaozinho = Jogador()
contador_pontos = 0
contador_morte = 0
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
        texto_pontuacao = fonte.render(f"Pontuação: {contador_pontos}", True,(255,255,255),None)
        tela.blit(texto_pontuacao,(0,0))
        limaozinho.andar(teclas_pressionadas)

        for frutaruim in lista_frutaruim:
            frutaruim.andar()
            frutaruim.exibir(tela)
            if limaozinho.mascara.overlap(frutaruim.mascara,(frutaruim.pos_y_frutaruim - limaozinho.pos_y, frutaruim.pos_x_frutaruim - limaozinho.pos_x)):
                frutaruim.voltar()
                limaozinho.ruim()
                limaozinho.voltar()
                contador_morte += 1
                if contador_morte ==6:
                    status_jogo = "PERDEU"
                    limaozinho.perdeu()
                    contador_morte = 0
                    contador_pontos = 0
        for frutaboa in lista_frutaboa:
            frutaboa.andar()
            frutaboa.exibir(tela)
            if limaozinho.mascara.overlap(frutaboa.mascara,(frutaboa.pos_x_frutaboa - limaozinho.pos_x, frutaboa.pos_y_frutaboa - limaozinho.pos_y)):
                contador_pontos = contador_pontos +1
                limaozinho.bom()
                frutaboa.voltar()
            if contador_pontos == 15:
                status_jogo = "GANHOU"
                limaozinho.ganhou()
                
    if status_jogo == "GANHOU":
        tela.blit(capa_ganhou,(0,0))
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"
            contador_pontos = 0
    
    if status_jogo == "PERDEU":
        tela.blit(capa_perdeu,(0,0))
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"
             
        


 
    

    # 4. Atualiza a tela para mostrar os desenhos novos
    pg.display.update()





