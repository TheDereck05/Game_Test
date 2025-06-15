import pygame
class Portal:
    def __init__(self, x, y, ancho, alto, color=(0, 0, 255)):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)

    def colision(self, jugador):
        jugador_rect = pygame.Rect(jugador.pos[0], jugador.pos[1], jugador.ancho, jugador.alto)
        return self.rect.colliderect(jugador_rect)
