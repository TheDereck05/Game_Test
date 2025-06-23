import os, pygame
from Personaje.Jugador import Cubo, Nave, Araña
from Portal import Portal
from gadgets import Trampolin, Orbe
from obtaculos import Pincho, PinchosMultiples, Cuadrado
from Portal import Portal
from final import mostrar_final
from menu import mostrar_seleccion_nivel


def juego_nivel_1(pantalla, reloj):

    proyect_dir = os.path.dirname(os.path.dirname(__file__))
    ruta_musica = os.path.join(proyect_dir, "assets", "nivel_1", "Music1.mp3")

# -------- Inicializar y reproducir música --------
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.set_volume(0.5)  # volumen entre 0.0 y 1.0
    pygame.mixer.music.play(-1)  # -1 para que suene en bucle
# -------------------------------------------------

    # — configuración inicial —
    suelo_y     = 675
    jugador     = Cubo(40, 40, [0, suelo_y-40], vida=1, velocidad=5)
    techo_y     = 0
    nivel_ancho = 4000
    pantalla_ancho = 450
    scroll_objetivo_x = 0
    scroll_actual_x = 0
    suavizado = 0.1

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
    portales = [
    Portal(687, 525, 5, 95, color=(255, 0, 255), tipo="araña")   # verde: convierte a nave
    
    ]


    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            jugador.saltar()

       # calculo de scroll
        pos_central = jugador.pos[0] + jugador.ancho//2
        scroll_objetivo_x = pos_central - pantalla_ancho//2
        scroll_objetivo_x = max(0, min(scroll_objetivo_x, nivel_ancho - pantalla_ancho))
        scroll_actual_x += (scroll_objetivo_x - scroll_actual_x) * suavizado
        scroll_x = int(scroll_actual_x) 
        # dibujar fondo y jugador
        for x in range(0, nivel_ancho, fondo.get_width()):
            pantalla.blit(fondo, (x - scroll_x, 0))

        for x in range(int(scroll_x//ancho_img) * ancho_img, int(scroll_x + pantalla_ancho) + ancho_img, ancho_img):
            pantalla.blit(suelo, (x-scroll_x, suelo_y))
                
        if jugador.modo_nave:
            jugador.volar(teclas, suelo_y)
        elif jugador.modo_araña:
            jugador.inversion(teclas[pygame.K_SPACE], suelo_y, techo_y)
        else:
            jugador.actualizar(suelo_y)
            jugador.movimiento_horizontal()

        # 1) dibujar y 2) procesar colisión en un solo bucle
        #    (cada objeto implementa su propio procesar_colision)
        for obs in obstaculos:
            obs.dibujar(pantalla,scroll_x)
            obs.procesar_colision(jugador, teclas)

        for gad in gadgets:
            gad.dibujar(pantalla,scroll_x)
            gad.procesar_colision(jugador, teclas)

        for port in portales:
            port.dibujar(pantalla,scroll_x)
            if port.colision(jugador):
                if port.tipo == "nave":
                    jugador = Nave(jugador.ancho, jugador.alto, jugador.pos, jugador.vida, jugador.velocidad)
                elif port.tipo == "cubo":
                    jugador = Cubo(jugador.ancho, jugador.alto, jugador.pos, jugador.vida, jugador.velocidad)
                elif port.tipo =="araña":
                    jugador =Araña(jugador.ancho, jugador.alto, jugador.pos, jugador.vida, jugador.velocidad)

                    
        jugador.dibujar(pantalla,scroll_x)
        

        if jugador.pos[0] >= nivel_ancho - 100:
            mostrar_final(pantalla, reloj)
            return mostrar_seleccion_nivel
        
        pygame.display.flip()
        reloj.tick(60)
