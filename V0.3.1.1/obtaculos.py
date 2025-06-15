import pygame

class Obstaculo:

    tipo_mortal = 1
    tipo_plataforma = 2
 
    def __init__(self,x ,y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.tipo = None

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 0, 0), self.rect)

    def colisiona_con(self, jugador_rect):
        return self.rect.colliderect(jugador_rect)
    
    def procesar_colision(self, jugador, teclas=None):
        pass

class Pincho(Obstaculo):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)
        #Se puede cambiar el color
        self.color = (255,0,0) #Amarillo
        self.tipo = Obstaculo.tipo_mortal
    def dibujar(self, pantalla):
        vertice_superior =    (self.rect.centerx, self.rect.top)
        vertice_inferior_izq =  (self.rect.left,  self.rect.bottom)
        vertice_inferior_der =  (self.rect.right, self.rect.bottom)

        puntos = [vertice_superior, vertice_inferior_izq, vertice_inferior_der]
        pygame.draw.polygon(pantalla, self.color, puntos)

    def procesar_colision(self, jugador, teclas=None):
        if self.colisiona_con(jugador.get_rect()):
            jugador.perder_vida()
            jugador.pos=[100,100]
            jugador.velocidad_vertical = 0
            jugador.en_suelo = False
        
class PinchosMultiples(Obstaculo):
    def __init__(self, x, y, ancho_total=40, alto=20, cantidad=3):
        super().__init__(x, y, ancho_total, alto)
        self.color = (255, 255, 0)  # Amarillo
        self.cantidad = cantidad
        self.ancho_pincho = ancho_total / cantidad
        self.tipo = Obstaculo.tipo_mortal

    def dibujar(self, pantalla):
        for i in range(self.cantidad):
            izquierda = self.rect.left + i * self.ancho_pincho
            derecha = izquierda + self.ancho_pincho
            centro = (izquierda + derecha) / 2

            vertice_superior = (centro, self.rect.top)
            vertice_inferior_izq = (izquierda, self.rect.bottom)
            vertice_inferior_der = (derecha, self.rect.bottom)

            puntos = [vertice_superior, vertice_inferior_izq, vertice_inferior_der]
            pygame.draw.polygon(pantalla, self.color, puntos)

    def procesar_colision(self, jugador, teclas=None):
        if self.colisiona_con(jugador.get_rect()):
            jugador.perder_vida()
            jugador.pos=[100,100]
            jugador.velocidad_vertical = 0
            jugador.en_suelo = False

class Cuadrado(Obstaculo):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)
        self.color = (128,50,12)
        self.tipo = Obstaculo.tipo_plataforma

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla,self.color, self.rect)

    def colision_lateral(self, rect_jugador):
        if not self.rect.colliderect(rect_jugador):
            return False
        centro_vertical_jugador = rect_jugador.centery
        return (self.rect.top < centro_vertical_jugador < self.rect.bottom)

    def colision_tope(self, rec_jugador, velocidad_vertical):
        if velocidad_vertical > 0:
            if rec_jugador.bottom >= self.rect.top and rec_jugador.bottom <= self.rect.top + 10:
                if rec_jugador.right > self.rect.left and rec_jugador.left < self.rect.right:
                    return True
        return False
    def procesar_colision(self, jugador, teclas=None):
        player = jugador.get_rect()
        # Choque por arriba
        if self.colision_tope(player, jugador.velocidad_vertical):
            jugador.pos[1] = self.rect.top - jugador.alto
            jugador.velocidad_vertical = 0
            jugador.en_suelo = True
        # Choque lateral
        elif self.colision_lateral(player):
            jugador.perder_vida()
            jugador.pos = [100, 100]
            jugador.velocidad_vertical = 0
            jugador.en_suelo = False