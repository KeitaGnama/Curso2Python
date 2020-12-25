#variable=atributo

class Circulo:
    def __init__(self,radio):
        self.radio=radio


#directiva de la propiedad
    @property
    def area(self):
          return 3.1416*(self.radio**2)
#objeto

c=Circulo(10)
print(c.area)