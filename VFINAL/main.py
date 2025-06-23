import pygame, sys, os
from menu import mostrar_menu
from juego_nivel_1.nivel1 import juego_nivel_1
from juego_nivel_1.musica import play_music

from juego_nivel_2.nivel2 import juego_nivel_2
from juego_nivel_2.musica import play_music

from juego_nivel_3.nivel3 import juego_nivel_3
from juego_nivel_3.musica import play_music

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((1200, 720))
    pygame.display.set_caption("Chasky Run")
    reloj = pygame.time.Clock()

    ruta_menu = os.path.join("assets", "Music_menu.mp3")
    play_music(ruta_menu)

    # mostrar_menu internamente llama a mostrar_seleccion_nivel
    accion = mostrar_menu(pantalla)

    if accion == "nivel_1":
        juego_nivel_1(pantalla, reloj)
        play_music(ruta_menu)
    elif accion == "nivel_2":
        juego_nivel_2(pantalla, reloj)
        play_music(ruta_menu)
    elif accion == "nivel_3":
        juego_nivel_3(pantalla, reloj)
        play_music(ruta_menu)


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

