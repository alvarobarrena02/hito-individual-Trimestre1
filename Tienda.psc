Algoritmo Tienda
	Repetir
		// mostrar menu
		Borrar Pantalla
		Escribir 'Elige una opci�n de la tienda:'
		Escribir '1 - Registrar cliente'
		Escribir '2 - Seleccionar productos'
		Escribir '3 - Pagar productos'
		Escribir '4 - Seguimiento del pedido'
		Escribir '5 - Salir'
		// introducir una opcion
		Leer Option
		// proceso del men�
		Segun Option  Hacer
			1:
				Escribir '*********** REGISTRO DEL CLIENTE ***********'
				Escribir 'Introduce los siguientes datos: '
				// nombre
				Escribir 'Introduce tu nombre: '
				Leer nombre
				// apellidos
				Escribir 'Introduce tus apellidos: '
				Leer apellidos
				// dni
				Escribir 'Introduce tu DNI: '
				Leer dni
				// telefono
				Escribir 'Introduce tu n�mero de m�vil: '
				Leer telefono
				// correo
				Escribir 'Introduce tu correo electr�nico: '
				Leer correo
				// pais
				Escribir 'Introduce tu pa�s: '
				Leer pais
				Escribir 'Guardando los datos...'
				Escribir 'Datos guardados correctamente'
			2:
				// menu productos
				Escribir 'Productos disponibles: '
				Escribir '1 - Camisetas'
				Escribir '2 - Pantalones'
				Escribir '3 - Zapatillas'
				Escribir '4 - Relojes'
				Escribir '5 - Calcetines'
				Escribir '6- Gorras'
				Escribir '0 - Salir de men� productos'
				Escribir 'Introduce una opci�n del 0 al 6...'
				Leer Option
				// input opcion
				Segun Option  Hacer
					1:
						Escribir '*********** SELECCI�N DE PRODUCTOS ***********'
						Escribir 'Introduce el n�mero de camisetas que quieres: '
						Leer camisetas
					2:
						Escribir 'Introduce el n�mero de pantalones que quieres: '
						Leer pantalones
					3:
						Escribir 'Introduce el n�mero de zapatillas que quieres: '
						Leer zapatillas
					4:
						Escribir 'Introduce el n�mero de relojes que quieres: '
						Leer relojes
					5:
						Escribir 'Introduce el n�mero de calcetines que quieres: '
						Leer calcetines
					6:
						Escribir 'Introduce el n�mero de gorras que quieres: '
						Leer gorras
					0:
						Escribir 'Saliendo del men� de productos...'
				FinSegun
			3:
				Escribir '*********** PAGO DE PRODUCTOS ***********'
				Definir nombreTarjeta Como Caracter
				Escribir 'Introduzca el nombre de la tarjeta: '
				Leer nombreTarjeta
				Definir numTarjeta Como Entero
				Escribir 'Introduzca el n�mero de la tarjeta: '
				Leer numTarjeta
				Definir cvvTarjeta Como Entero
				Escribir 'Introduzca el CVV de la tarjeta: '
				Leer cvvTarjeta
				Escribir 'Esperando confirmaci�n...'
				Escribir 'Pago aceptado correctamente'
				Escribir 'Se le enviar� la factura al correo: ',correo
				Escribir '*****************************************'
			4:
				Escribir 'El seguimiento de su pedido se env�o correctamente a su correo ',correo,'y a su n�mero de tel�fono: ',telefono
		FinSegun
		Escribir 'Pulsa la tecla enter para continuar'
		Esperar Tecla
	Hasta Que Option=5
FinAlgoritmo
