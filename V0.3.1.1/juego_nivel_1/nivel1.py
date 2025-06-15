import os, pygame
from Personaje.Jugador import Cubo, Nave, Araña
from Portal import Portal
from gadgets import Trampolin, Orbe
from obtaculos import Pincho, PinchosMultiples, Cuadrado

def juego_nivel_1(pantalla, reloj):
    # — configuración inicial —
    jugador     = Cubo(40, 40, [100, 400], vida=1, velocidad=5)
    portal      = Portal(687, 525, 5, 95)
    suelo_y     = 675
    nivel_ancho = 2000

    # carga fondo
    proyecto_dir = os.path.dirname(os.path.dirname(__file__))
    ruta_fondo   = os.path.join(proyecto_dir, "assets", "nivel_1", "Nivel_1.jpg")
    ruta_suelo   = os.path.join(proyecto_dir, "assets", "nivel_1", "suelo_nivel_1.jpg")
    fondo        = pygame.image.load(ruta_fondo).convert()

#-------------------------------------------------------------------------.
    suelo        = pygame.image.load(ruta_suelo).convert()
    ancho_img    = suelo.get_width()
#-------------------------------------------------------------------------.

    # crea lista de obstáculos y gadgets UNA VEZ
    obstaculos = [
        PinchosMultiples(400,  suelo_y - 20, ancho_total=40, alto=20, cantidad=3),
        Cuadrado(       600,  suelo_y - 40, ancho=40, alto=40),
        Cuadrado(       640,  suelo_y - 40, ancho=40, alto=40),
        Pincho(         700,  suelo_y - 20, ancho=40, alto=20),  # ejemplo extra
    ]
    gadgets = [
        Trampolin(500,  suelo_y - 10, ancho_total=40, alto=10),
        Orbe(     802,  suelo_y - 75, ancho_total=22, alto=22),
    ]

    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            jugador.saltar()

        # dibujar fondo y jugador
        pantalla.blit(fondo, (0, 0))
        #Dibujar Suelo Visible:
        for x in range(0,1200, ancho_img):

            pantalla.blit(suelo, (x, suelo_y))
                
        jugador.actualizar(suelo_y)
        jugador.movimiento_horizontal()

        # calculo de scroll
        scroll_x = max(0, min(jugador.pos[0] - 950, nivel_ancho - 800))

        # 1) dibujar y 2) procesar colisión en un solo bucle
        #    (cada objeto implementa su propio procesar_colision)
        for obs in obstaculos:
            obs.dibujar(pantalla)
            obs.procesar_colision(jugador, teclas)
        for gad in gadgets:
            gad.dibujar(pantalla)
            gad.procesar_colision(jugador, teclas)

        # dibujar portal y jugador
        portal.dibujar(pantalla)
        jugador_rect = jugador.get_rect()
        pygame.draw.rect(pantalla, (255, 125, 175), jugador_rect)
        
        pygame.display.flip()
        reloj.tick(60)


