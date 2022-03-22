
def suma():
    n1 = int(input("Introduce tu primer número: ") )
    n2 = int(input("Introduce tu segundo número: ") )
    res = n1+n2

    print(f'La suma es: {n1} + {n2} = {res}')

suma()

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Hacer otra suma
    2) Salir
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        n1 = int(input("Introduce tu primer número: ") )
        n2 = int(input("Introduce tu segundo número: ") )
        res = n1+n2
        print(f'La suma es: {n1} + {n2} = {res}')
    elif opcion == 2:
        break
    else:
        print("Opción incorrecta")