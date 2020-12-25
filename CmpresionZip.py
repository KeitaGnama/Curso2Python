import zipfile
from zipfile import ZipFile
with zipfile.ZipFile('archivo.zip','w') as fzip:
    fzip.write('Doc2.docx')
    fzip.write('PORTADA.docx')
    #fzip.write('PythonL.jpg')
    fzip.printdir()
    fzip.extractall()