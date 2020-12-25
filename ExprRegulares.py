#Expresiones regulares son secuentracia de carracteres que forman un patron para realizar busqueda.
#tmb con manejo de cadenas (cualquier conjunto de carracteres)
#regex=ER , el modulo "re" nos ayuda para realizar la busqueda
#clasificacion des ER: (alternacion,cuantificacion,agrupacion)


#Patrones : nos sirve para componer una ER para realizar uan busqueda

"""import re

patron=re.compile("\d\d\d")
print (re.search(r"\d\d\d","kilo912metro").group())"""

"""import re 
if(re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
    print("se encontro el patron")"""

"""import re  
print (re.sub(r"\d","*","mpangSuera990",2))"""

import re 
regex = re.compile(r"ab",re.IGNORECASE)
print (regex.search("jutnmilajAbuimmnhtr"))




