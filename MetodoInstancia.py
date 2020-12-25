class Persona():
    edad=18
    def __init__(self,nombre,nacionalidad):
        self.nombre=nombre
        self.nacionalidad=nacionalidad
    

    def nadar(self):
        print('estoy nadando')


personal=Persona("jose",'Mexicano')
personal.nadar()