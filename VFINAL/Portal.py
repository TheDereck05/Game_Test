import pygame

class Portal:
    def __init__(self, x, y, ancho, alto, color=(0, 0, 255), tipo="nada"):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color
        self.tipo = tipo

    def dibujar(self, pantalla, scroll_x = 0):
        rect_visible = pygame.Rect(self.rect.x - scroll_x, self.rect.y, self.rect.width, self.rect.height)

        if -self.rect.width < rect_visible.x < pantalla.get_width():
            pygame.draw.rect(pantalla, self.color, rect_visible)

    def colision(self, jugador):
        jugador_rect = pygame.Rect(jugador.pos[0], jugador.pos[1], jugador.ancho, jugador.alto)
        return self.rect.colliderect(jugador_rect)

class PortalVerde(Portal):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto, color=(0, 255, 0))  # color verde

    def colision(self, jugador):
        jugador_rect = pygame.Rect(jugador.pos[0], jugador.pos[1], jugador.ancho, jugador.alto)
        return self.rect.colliderect(jugador_rect)
    
class PortalRojo(Portal):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto, color=(255, 0, 0))  # rojo

    def colision(self, jugador):
        jugador_rect = pygame.Rect(jugador.pos[0], jugador.pos[1], jugador.ancho, jugador.alto)
        return self.rect.colliderect(jugador_rect)


class PortalRosa(Portal):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto, color=(255, 0, 255))  # rosa

    def colision(self, jugador):
        jugador_rect = pygame.Rect(jugador.pos[0], jugador.pos[1], jugador.ancho, jugador.alto)
        return self.rect.colliderect(jugador_rect)


