#Programacion Funcuional(basada funciones matematicas) : ventaja (mas confiable,menos problema de depuracion)
#lenguages funcionales
#caracteristicas de PF (recursividad,orden superior)
#en PF nos encontramos con 3 funciones filter(),reduce() y map()
"""def  lower(elementos):return elementos.lower()

lista=["KEITA","GNAMa","No"]
print(list(map(lower,lista)))

print([cad.lower() for cad in lista])"""

 #funcion orden superior
def saludo(idioma):
    def saludo_es():
        print("Hola")
    def saludo_en():
        print("Hi")
    idioma_func={"es":saludo_es,
                 "en":saludo_en
                 }
    return idioma_func[idioma]
saludar=saludo("es")
saludar()
