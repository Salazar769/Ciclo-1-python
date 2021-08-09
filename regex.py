"""
contraseña cuenta requwriientos

"""
import re 

contraseña= input("texto")

codigo = re.compile("[A-Z]{4}[a-z][0-9]+")

val1 = codigo.fullmatch(contraseña)

if val1 :
    print("contraseña correcta")
else:
    print("tu madre")

while True:
    contraseña= input("texto")

    codigo = re.compile("/([A-Z]{4}[a-z][0-9]+/)")

    val1 = codigo.fullmatch(contraseña)

    if val1 :
        print("contraseña correcta")
    else:
        print("tu madre")
