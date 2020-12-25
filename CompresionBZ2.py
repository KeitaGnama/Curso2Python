import bz2
cadena=b"cadena cadena cadena cadena"
cadena_c=bz2.compress(cadena)

print(cadena_c)
print(bz2.decompress(cadena_c))