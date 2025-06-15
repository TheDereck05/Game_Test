import pygame
import sys

# Colores
BLANCO = (255, 255, 255)
NEGRO  = (0, 0, 0)
AZUL   = (0, 100, 255)
GRIS   = (50, 50, 50)

def botones_horizontal(pantalla, opciones, fuente, mouse_pos):
    rects = []
    ancho_boton   = 200
    alto_boton    = 60
    espacio_entre  = 40
    
    # Calcular ancho total de todos los botones más espacios
    total_ancho = len(opciones) * ancho_boton + (len(opciones) - 1) * espacio_entre
    inicio_x = (pantalla.get_width() - total_ancho) // 2

    # Y fijo para centrar verticalmente
    centrar_y = pantalla.get_height() // 2
    y_boton = centrar_y - alto_boton // 2

    for i, texto in enumerate(opciones):
        # X de este botón
        x_boton = inicio_x + i * (ancho_boton + espacio_entre)

        # Rectángulo del botón
        rect = pygame.Rect(x_boton, y_boton, ancho_boton, alto_boton)

        # Detectar si el ratón está encima de este rect
        hover = rect.collidepoint(mouse_pos)

        # Elegir color de fondo: AZUL si hover, GRIS en caso contrario
        color_fondo = AZUL if hover else GRIS

        # Dibujar rectángulo redondeado
        pygame.draw.rect(pantalla, color_fondo, rect, border_radius=8)

        # Renderizar el texto en blanco centrado dentro del rect
        render = fuente.render(texto, True, BLANCO)
        txt_rect = render.get_rect(center=rect.center)
        pantalla.blit(render, txt_rect)

        # Guardar (texto, rect) para detectar clics
        rects.append((texto, rect))

    return rects


def mostrar_menu(pantalla):
    pygame.font.init()
    fuente = pygame.font.SysFont("arial", 36)
    reloj  = pygame.time.Clock()

    opciones = ["Jugar", "Salir"]
    ejecutando = True

    while ejecutando:
        pantalla.fill(NEGRO)
        mouse_pos = pygame.mouse.get_pos()

        # 1) Dibujar los botones horizontalmente y recopilar sus rects
        rects_opciones = botones_horizontal(pantalla, opciones, fuente, mouse_pos)

        # 2) Manejo de eventos solo con ratón
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # clic izquierdo
                    for texto, rect in rects_opciones:
                        if rect.collidepoint(mouse_pos):
                            if texto == "Jugar":
                                return "jugar"
                            elif texto == "Salir":
                                pygame.quit()
                                sys.exit()

        pygame.display.flip()
        reloj.tick(60)




