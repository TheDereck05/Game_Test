import pygame

class Cubo:
   def __init__( self, ancho, alto, pos, vida, velocidad):
      self.vida = 1 
      self.pos = pos # esta es la lista [x,y]
      self.ancho = ancho
      self.alto = alto
      self.velocidad = velocidad
      self.velocidad_vertical = 0
      self.gravedad = 1
      self.fuerza_salto= 12
      self.en_suelo=True
      self.modo_nave = False  
      self.modo_araña = False

   def saltar(self):
      if self.en_suelo:
         self.velocidad_vertical = -self.fuerza_salto
         self.en_suelo= False

   def perder_vida(self):
       self.vida -=1 
       
   def movimiento_horizontal(self):
      self.pos[0] += self.velocidad

   def actualizar(self, suelo_y):
      self.velocidad_vertical += self.gravedad
      self.pos[1] += self.velocidad_vertical
      
      if self.pos[1] > suelo_y - self.alto:
         self.pos[1] = suelo_y - self.alto
         self.velocidad_vertical = 0
         self.en_suelo = True
         
   def dibujar(self, pantalla, scroll_x):
        pos_x = int(round(self.pos[0] - scroll_x))
        pos_y = int(round(self.pos[1]))

        if (pos_x + self.ancho > 0 and pos_x < pantalla.get_width() and 
        pos_y + self.alto > 0 and pos_y < pantalla.get_height()):
            pygame.draw.rect(
                pantalla,
                (255, 125, 175),
                (pos_x, pos_y, self.ancho, self.alto)
         )
       
   def get_rect(self):
       return pygame.Rect(self.pos[0], self.pos[1], self.ancho, self.alto)

class Nave(Cubo):
   def __init__( self, ancho, alto, pos, vida, velocidad):
         super().__init__(ancho, alto, pos, vida, velocidad)
         self.modo_nave= True
         self.modo_araña = False

   def volar(self, teclas, suelo_y):
      if teclas[pygame.K_SPACE]:
         self.velocidad_vertical -= 5
      else:
         self.velocidad_vertical += self.gravedad

      self.velocidad_vertical = max(min(self.velocidad_vertical, 10), -10)
      self.pos[1] += self.velocidad_vertical
          # Verificar si toca el suelo
      if self.pos[1] > suelo_y - self.alto:
         self.pos[1] = suelo_y - self.alto
         self.velocidad_vertical = 0
      self.movimiento_horizontal()

class Araña(Cubo):
    def __init__(self, ancho, alto, pos, vida, velocidad):
        super().__init__(ancho, alto, pos, vida, velocidad)
        self.modo_araña = True
        self.modo_nave = False
        self.en_techo = False
        self.en_transicion = False  # Para evitar múltiples cambios al dejar presionada la tecla

    def inversion(self, tecla_presionada, suelo_y, techo_y):
        if tecla_presionada and not self.en_transicion:
            self.en_techo = not self.en_techo
            self.en_transicion = True  # Evita más cambios hasta soltar la tecla

            if self.en_techo:
                self.pos[1] = techo_y
            else:
                self.pos[1] = suelo_y - self.alto

        elif not tecla_presionada:
            self.en_transicion = False  # Ya soltó la tecla, puede cambiar de nuevo

        self.movimiento_horizontal()

    def actualizar(self, suelo_y, techo_y):
        # No se usa la gravedad en la araña, solo se posiciona en el techo o el suelo
        if self.en_techo:
            self.pos[1] = techo_y
        else:
            self.pos[1] = suelo_y - self.alto
