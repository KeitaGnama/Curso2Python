import tarfile
archivo_k=tarfile.open('primer.tar.gz','w:gz')
archivo_k.add('PORTADA.docx')
archivo_k.add('Doc2.docx')
archivo_k.close()