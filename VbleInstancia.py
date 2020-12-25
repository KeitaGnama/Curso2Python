class Persona():
    edad=18
    def __init__(self,nombre,nacionalidad):
        self.nombre=nombre
        self.nacionalidad=nacionalidad


personal=Persona("jose",'Mexicano')

print(personal.nombre)