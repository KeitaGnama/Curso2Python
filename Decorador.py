


def primerD(funcion):
    def FuncionDecorada(*args,**kkwars):
        print("primer decorador")
    return FuncionDecorada

@primerD
def funcion():
    print("mi primer decorador")
funcion()