import pygame

current_music = None
volume = 0.5

def play_music(ruta):
    global current_music
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    if current_music != ruta:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
            current_music = ruta

def stop_music():
    global current_music
    pygame.mixer.music.stop()
    current_music = None

def set_volume(nivel):
    global volume
    volume = max(0.0, min(nivel / 10.0, 1.0))
    pygame.mixer.music.set_volume(volume)

def get_volume():
    return int(volume * 10)
