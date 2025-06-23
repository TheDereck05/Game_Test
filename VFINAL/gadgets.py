import pygame
from Personaje.Jugador import Cubo, Nave, Araña
from obtaculos import Obstaculo

class Gadget:
    
    def __init__(self,x ,y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = (255, 0, 0)
    def dibujar(self, pantalla, scroll_x = 0):
        rect_visible = pygame.Rect(
            self.rect.x - scroll_x,
            self.rect.y,
            self.rect.width,
            self.rect.height
        )
        if -self.rect.width < rect_visible.x < pantalla.get_width():
            pygame.draw.rect(pantalla, self.color, rect_visible)

    def colisiona_con(self, jugador_rect):
        return self.rect.colliderect(jugador_rect)
    

    def procesar_colision(self, jugador, teclas=None):
        pass
        

class Trampolin(Gadget):
    tipo_trampolin = "trampolin"
    def __init__(self, x, y, ancho_total=40, alto=20):
        super().__init__(x, y, ancho_total, alto)
        self.color = (75, 205, 95) 
        self.mortal = Obstaculo.tipo_plataforma
        self.tipo = Trampolin.tipo_trampolin
        self.posicion_original = (x,y)

    def dibujar(self, pantalla, scroll_x = 0):
        rect_visible = pygame.Rect(
            self.rect.x - scroll_x,
            self.rect.y,
            self.rect.width,
            self.rect.height
        )
        if -self.rect.width < rect_visible.x < pantalla.get_width():
            pygame.draw.ellipse(pantalla, self.color, rect_visible)

    def procesar_colision(self, jugador, teclas=None):
        if self.colisiona_con(jugador.get_rect()):
            jugador.velocidad_vertical = -jugador.fuerza_salto * 1.5
            jugador.en_suelo = False

class Orbe(Gadget):
    tipo_orbe = "orbe"
    def __init__(self, x, y, ancho_total=40, alto=20):
        super().__init__(x, y, ancho_total, alto)
        self.color = (145, 45, 152) 
        self.mortal = Obstaculo.tipo_plataforma
        self.tipo = Orbe.tipo_orbe

    def dibujar(self, pantalla, scroll_x = 0):
        rect_visible = pygame.Rect(
            self.rect.x - scroll_x,
            self.rect.y,
            self.rect.width,
            self.rect.height
        )
        if -self.rect.width < rect_visible.x < pantalla.get_width():
            pygame.draw.ellipse(pantalla, self.color, rect_visible)
            pygame.draw.circle(pantalla, (255,255,255), rect_visible.center, 5)

    def procesar_colision(self, jugador, teclas=None):
        if self.colisiona_con(jugador.get_rect()) and teclas[pygame.K_SPACE]:
            jugador.velocidad_vertical = -jugador.fuerza_salto * 1.5
            jugador.en_suelo = False
        
    