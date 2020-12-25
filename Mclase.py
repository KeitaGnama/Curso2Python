class Persona():
    def __init__(self):
        pass
    
    def despedir(self):
        print("adios")
        
    @classmethod        
    def saludar(cls,nombre):
        print("estoy saludable \n"  +nombre)
Persona.saludar("keita")