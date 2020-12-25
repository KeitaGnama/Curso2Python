class Persona():
    def __init__(self):
        pass
    def brincar(self):
        print("Brinco")
    @classmethod
    def correr(cls):
        print("Corro")
    @staticmethod
    def nadar():
        print("Nado")
Jose=Persona()
Jose.nadar()