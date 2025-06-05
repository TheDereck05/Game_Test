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

  def saltar(self):
     if self.en_suelo:
       self.velocidad_vertical = self.fuerza_salto
       self.en_suelo= False
  def movimiento_horizontal(self):
      self.pos[0] += self.velocidad

  def actualizar(self, suelo_y):
      self.velocidad_vertical += self.gravedad
      self.pos[1] += self.velocidad_vertical
      
      if self.pos[1] > suelo_y - self.alto:
         self.pos[1] = suelo_y - self.alto
         self.velocidad_vertical = 0
         self.en_suelo = True

class Nave(Cubo):
   def __init__( self, ancho, alto, pos, vida, velocidad):
        super().__init__(ancho, alto, pos, vida, velocidad)
        self.modo_nave= True

   def volar( self, tecla_presionada):
        if tecla_presionada:
           self.velocidad_vertical += 5
        else:
           self.velocidad_vertical -= self.gravedad 
        self.pos[1] += self.velocidad_vertical
        self.movimiento_horizontal()

class Araña(Cubo):
   def __init__( self, ancho, alto, pos, vida, velocidad):
        super().__init__(ancho, alto, pos, vida, velocidad)
        self.modo_araña= True
        self.en_techo= False
   def inversion( self, tecla_presionada, suelo_y, techo_y):
        if tecla_presionada:

           if self.en_techo:
               self.pos[1] = suelo_y - self.alto
               self.en_techo= False
           else:
              self.pos[1] = techo_y
              self.en_techo = True

        self.movimiento_horizontal()