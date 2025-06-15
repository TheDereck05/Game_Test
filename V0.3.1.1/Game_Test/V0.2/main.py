import pygame
from Personaje.Jugador import Cubo, Nave, Araña
from menu import mostrar_menu

# Inicializar pygame y pantalla
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battle Game")  # Opcional
reloj = pygame.time.Clock()

# Mostrar menú y esperar decisión
accion = mostrar_menu(pantalla)

if accion == "jugar":
    # Crear jugador (puedes intercambiar entre Cubo, Nave, Araña)
    jugador = Cubo(40, 40, [100, 100], vida=3, velocidad=5)
    suelo_y = 500
    jugando = True

    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            jugador.saltar()

        pantalla.fill((30, 30, 30))

        jugador.actualizar(suelo_y)
        jugador.movimiento_horizontal()

        pygame.draw.rect(pantalla, (200, 0, 0), (*jugador.pos, jugador.ancho, jugador.alto))
        pygame.display.flip()
        reloj.tick(60)

pygame.quit()
