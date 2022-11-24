import os
import time
os.system('cls')

def tienda():
    try:
        menu = int(input(""" 
*********** BIENVENIDO A LA TIENDA ***********
Elige una opción de la tienda:\n
        1 - Registrar cliente
        2 - Seleccionar productos
        3 - Pagar productos
        4 - Seguimiento del pedido
        5 - Salir
        """))
        #Datos del cliente
        nombre = []
        apellidos = []
        dni = []
        telefono = []
        correo = []
        pais = []

        while menu != 5:
            if menu == 1:
                print('*********** REGISTRO DEL CLIENTE ***********')
                print('Introduce los siguientes datos: ')
                nombre.append(input('Introduce tu nombre: '))
                apellidos.append(input('Introduce tus apellidos: '))
                dni.append(input('Introduce tu DNI: '))
                try:
                    telefono.append(int(input('Introduce tu número de móvil: ')))
                except:
                    print('Has introducido un carácter que no es un número, introduzca un número para poder continuar')
                    telefono.append(int(input('Introduce tu número de móvil: ')))
                correo.append(input('Introduce tu correo electrónico: '))
                if "@" in correo:
                    print("Es válido")
                    correo.append()
                    print(correo)
                else:
                    print("No es válido, introduce un correo válido")
                    time.sleep(2)
                    correo.append(input('Introduce tu correo electrónico: '))

                pais.append(input('Introduce tu país: '))
                print('Guardando los datos...')
                time.sleep(1)
                print('Datos guardados correctamente')
                print('Volviendo al menú...')
                time.sleep(2)
                print('**********************************************')

            elif menu == 2:
                print('*********** SELECCIÓN DE PRODUCTOS ***********')

                # Productos
                camisetas = []
                pantalones = []
                zapatillas = []
                relojes = []
                calcetines = []
                gorras = []

                opcion = input(""" 
Productos disponibles:\n
    1 - Camisetas 
    2 - Pantalones
    3 - Zapatillas
    4 - Relojes
    5 - Calcetines
    6 - Gorras 
    0 - Salir del menú de productos
                """)
                print('**********************************************')

                while opcion != 0:
                    if opcion == 1:
                        camisetas = int(input('Introduce el número de camisetas que quieres: '))
                        print(f'Se han guardado en el carrito {camisetas} camisetas')
                    elif opcion == 2:
                        pantalones = int(input('Introduce el número de pantalones que quieres: '))
                        print(f'Se han guardado en el carrito {pantalones} pantalones')
                    elif opcion == 3:
                        zapatillas = int(input('Introduce el número de zapatillas que quieres: '))
                        print(f'Se han guardado en el carrito {zapatillas} zapatillas')
                    elif opcion == 4:
                        relojes = int(input('Introduce el número de relojes que quieres: '))
                        print(f'Se han guardado en el carrito {relojes} relojes')
                    elif opcion == 5:
                        calcetines = int(input('Introduce el número de calcetines que quieres: '))
                        print(f'Se han guardado en el carrito {calcetines} calcetines')
                    elif opcion == 6:
                        gorras = int(input('Introduce el número de gorras que quieres: '))
                        print(f'Se han guardado en el carrito {gorras} gorras')
                    elif opcion == 0:
                        print('Saliendo del menú de productos')
                        exit
                    else:
                        print('Introduce una opción del 1 al 6')
                    opcion = input(""" 
Productos disponibles:\n
    1 - Camisetas 
    2 - Pantalones
    3 - Zapatillas
    4 - Relojes
    5 - Calcetines
    6 - Gorras 
    0 - Salir del menú de productos
                            """)

            elif menu == 3:
                print('*********** PASARELA DE PAGO DE LOS PRODUCTOS ***********')
                nombreTarj = input('Introduzca el nombre de la tarjeta: ')
                numTarj = int(input('Introduzca el número de la tarjeta: '))
                cvvTarj = int(input('Introduczca el CVV de la tarjeta: '))
                print('Esperando confirmación...')
                time.sleep(2)
                print('Pago aceptado correctamente')
                time.sleep(2)
                print('Volviendo al menú principal...')
                time.sleep(2)
                print('*********************************************************')

            elif menu == 4:
                print('*********** SEGUIMIENTO DEL PEDIDO ***********')
                print(f'El seguimiento de su pedido ha sido enviado al número {telefono} y al correo {correo} como PDF')
                time.sleep(5)
                print('**********************************************')

            else:
                print('Introduce una opción del 1 al 5')

            menu = int(input(""" 
Elige una opción de la tienda:\n
        1 - Registrar cliente
        2 - Seleccionar productos
        3 - Pagar productos
        4 - Seguimiento del pedido
        5 - Salir
            """))
    except:
        print('¡Error! Saliendo de la aplicación, vuelva a ejecutarla de nuevo')
tienda()