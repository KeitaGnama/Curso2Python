class Err(Exception):
    def __init__(self,valor):
        print("fue el error por", valor)
try:
    raise Err(4)
except Err:
    print("error escrito:")