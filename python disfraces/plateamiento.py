# Mensaje de bienvenida a la fiesta.
print("¡Bienvenido a la fiesta de disfraces temática NEON!")

# Inicializar contadores para el seguimiento de asistentes.
admitidos = 0
rechazados = 0

# Comienza un bucle infinito que permite ingresar los datos de los asistentes.
while True:
    # Solicita al usuario que ingrese su nombre o la palabra "salir" para finalizar.
    nombre = input("Por favor, ingresa tu nombre (o 'salir' para finalizar):")

    # Verifica si el usuario ingresó "salir" para finalizar el programa.
    if nombre.lower() == 'salir':
        break

    # Solicita la edad del usuario.
    edad = int(input("Por favor, ingresa tu edad: "))

    # Comprueba si el usuario es menor de 18 años y, en caso que si sea pasa y si no lo rechaza.
    if edad < 18:
        print("Lo siento, debes ser mayor de 18 años para ingresar.")
        rechazados += 1
    else:
        # Si el usuario es mayor de 18 años, pregunta si está disfrazado con la temática NEON.
        tematica = input("¿Estás disfrazado/a de la temática NEON? (Si/No): ")
        
        # Si no está disfrazado, se le rechaza.
        if tematica.lower() != 'si':
            print("Lo siento, debes estar disfrazado/a de la tematica NEON para ingresar.")
            rechazados += 1
        else:
            # Pide al usuario que ingrese la hora de ingreso.
            hora = int(input("Por favor, ingresa la hora de ingreso : "))
            
            # Comprueba si la hora de ingreso es posterior a las 12 de la noche y, en caso contrario, rechaza al usuario.
            if hora > 12 and hora < 6:
                print("Lo siento, el ingreso es permitido solo hasta las 12 de la noche.")
                rechazados += 1
            else:
                # Pregunta si el usuario lleva bebidas alcohólicas con el.
                bebidas_alcoholicas = input("¿Llevas bebidas alcoholicas contigo? (Si/No): ")
                
                # Si el usuario lleva bebidas alcohólicas, se le rechaza.
                if bebidas_alcoholicas.lower() == 'si':
                    print("Lo siento, no se permiten bebidas alcoholicas en la fiesta.")
                    rechazados += 1
                else:
                    # Si el usuario cumple con todos los requisitos, se le da la bienvenida a la fiesta.
                    print(f"¡Bienvenido a la fiesta, {nombre}! Disfruta la noche.")
                    admitidos += 1

# Muestra un resumen de asistentes al final del programa.
print("Resumen de asistentes:")
print(f"Asistentes admitidos: {admitidos}")
print(f"Asistentes rechazados: {rechazados}")
