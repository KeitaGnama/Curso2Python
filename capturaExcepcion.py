lista=[2,4,7,8,9]

try:
    print(lista[4])
except IndexError:
    print("Error: error en el indices")
else:
    print("no hay error")
finally:
    print("se ejecuto")
