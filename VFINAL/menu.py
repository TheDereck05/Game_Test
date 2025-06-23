import pygame
import sys
import os 
# Colores
BLANCO = (255, 255, 255)
AZUL   = (0, 100, 255)
GRIS   = (50, 50, 50)

def botones_horizontal(pantalla, opciones, fuente, mouse_pos):
    rects = []
    ancho_boton   = 200
    alto_boton    = 60
    espacio_entre  = 40
    
    total_ancho = len(opciones) * ancho_boton + (len(opciones) - 1) * espacio_entre
    inicio_x    = (pantalla.get_width() - total_ancho) // 2
    y_boton     = pantalla.get_height() // 2 - alto_boton // 2

    for i, texto in enumerate(opciones):
        x_boton   = inicio_x + i * (ancho_boton + espacio_entre)
        rect      = pygame.Rect(x_boton, y_boton, ancho_boton, alto_boton)
        hover     = rect.collidepoint(mouse_pos)
        color_fon = AZUL if hover else GRIS

        pygame.draw.rect(pantalla, color_fon, rect, border_radius=8)
        render    = fuente.render(texto, True, BLANCO)
        txt_rect  = render.get_rect(center=rect.center)
        pantalla.blit(render, txt_rect)
        rects.append((texto, rect))

    return rects

def mostrar_menu(pantalla):
    """Menú principal: Jugar o Salir"""
    pygame.font.init()
    fuente = pygame.font.SysFont("arial", 36)
    reloj  = pygame.time.Clock()

    proyecto_dir = os.path.dirname(__file__)
    ruta_fondo   = os.path.join(proyecto_dir, "assets", "menu", "menu_fondo.jpg")
    fondo = pygame.transform.scale(pygame.image.load(ruta_fondo).convert(), pantalla.get_size())



    opciones = ["Jugar", "Salir"]

    while True:
        pantalla.blit(fondo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        rects = botones_horizontal(pantalla, opciones, fuente, mouse_pos)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for texto, rect in rects:
                    if rect.collidepoint(mouse_pos):
                        if texto == "Jugar":
                            return mostrar_seleccion_nivel(pantalla)
                        elif texto == "Salir":
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()
        reloj.tick(60)

def mostrar_seleccion_nivel(pantalla):
    """Sub-menú de niveles"""
    pygame.font.init()
    fuente = pygame.font.SysFont("arial", 36)
    reloj  = pygame.time.Clock()
    opciones = ["Nivel 1", "Nivel 2", "Nivel 3", "Volver"]

    proyecto_dir = os.path.dirname(__file__)
    ruta_fondo   = os.path.join(proyecto_dir, "assets", "menu", "menu_fondo.jpg")
    fondo = pygame.transform.scale(pygame.image.load(ruta_fondo).convert(), pantalla.get_size())

    while True:
        pantalla.blit(fondo, (0, 0)) 
        mouse_pos = pygame.mouse.get_pos()
        rects = botones_horizontal(pantalla, opciones, fuente, mouse_pos)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for texto, rect in rects:
                    if rect.collidepoint(mouse_pos):
                        if texto == "Nivel 1":
                            return "nivel_1"
                        elif texto == "Nivel 2":
                            return "nivel_2"
                        elif texto == "Nivel 3":
                            return "nivel_3"
                        
                        elif texto == "Volver":
                            return mostrar_menu(pantalla)

        pygame.display.flip()
        reloj.tick(60)

# Ejemplo de uso en tu main.py
if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((1200, 720))
    accion = mostrar_menu(pantalla)

    # Aquí ya recibes, por ejemplo, "nivel_1"
    if accion == "nivel_1":
        # Lanza tu lógica de juego para el nivel 1
        print("¡Arrancando Nivel 1!") 
    elif accion == "nivel_2":
        print("¡Arrancando Nivel 2!") 
    elif accion == "nivel_3":
        print("¡Arrancando Nivel 3!") 






