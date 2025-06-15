import pygame, sys
from menu import mostrar_menu
from juego_nivel_1.nivel1 import juego_nivel_1

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((1200, 720))
    pygame.display.set_caption("Chasky Run")
    reloj = pygame.time.Clock()

    # mostrar_menu internamente llama a mostrar_seleccion_nivel
    accion = mostrar_menu(pantalla)

    if accion == "nivel_1":
        juego_nivel_1(pantalla, reloj)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

