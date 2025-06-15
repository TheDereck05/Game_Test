import pygame
from Personaje.Jugador import Cubo, Nave, Araña
from obtaculos import Obstaculo

class Gadget:
    
    def __init__(self,x ,y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 0, 0), self.rect)
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

    def dibujar(self, pantalla):
        # Dibujar una elipse blanca 
        pygame.draw.ellipse(pantalla, self.color, self.rect)

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

    def dibujar(self, pantalla):
        # Dibujar una elipse blanca 
        pygame.draw.ellipse(pantalla, self.color, self.rect)

    def procesar_colision(self, jugador, teclas=None):
        if self.colisiona_con(jugador.get_rect()) and teclas[pygame.K_SPACE]:
            jugador.velocidad_vertical = -jugador.fuerza_salto * 1.5
            jugador.en_suelo = False
        
    


