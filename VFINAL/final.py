import pygame, sys

def mostrar_final(pantalla, reloj):
    fuente = pygame.font.SysFont("arial", 64)
    texto = fuente.render("¡Nivel Completado!", True, (255, 255, 255))
    rect = texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))

    espera = True
    while espera:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                espera = False  # presionar una tecla para salir

        pantalla.fill((0, 0, 0))
        pantalla.blit(texto, rect)
        pygame.display.flip()
        reloj.tick(60)