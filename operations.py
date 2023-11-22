

# String operations
print("A" + "BC")
# print("A" + 1) cannot concatenate str and int


print("A" * 3)
print(3 * "A")



# Multiline string
greeting = '''\
Hello

How are you\
'''
print(greeting)

# String interpolation
name = "Mark"

print(f"This is my name {name}")

# rstrip

str = '     python  '
print(str.rstrip(), "hello")



while True:
    print( "Introduzca una puntuación utilizando un número del 1 al 5. Introduzca '6' para salir" )
    point = input()
    if point.isdecimal():
        point = int(point)
        if point == 6:
            print( "Terminación." )
            break
        elif 1 <= point <= 5:
            print( "Introduzca sus comentarios." )
            comment = input()
            print( f"Sus puntos.: {point}" )
            print( f"Tu comentario.: {comment}" )
    else:
        print( "Introduzca un número" )