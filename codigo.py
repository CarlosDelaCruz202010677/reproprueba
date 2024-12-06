def calculadora():
    print("¡Bienvenido a la calculadora!")
    print("Operaciones disponibles:")
    #print("1. Suma (+)")
    print("2. Resta (-)")
    print("otras opciones")
    print("4. División (/)")
    print("6. esta es una linea de prueba para la opcion salir")
    print("7. otra prueba")

    while True:
        try:
            # Solicitar números
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            
            # Solicitar operación
            operacion = input("Introduce la operación (+, -, *, /): ").strip()
            
            # Realizar la operación
            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                    continue
                resultado = num1 / num2
            else:
                print("Operación no válida. Intenta de nuevo.")
                continue
            
            print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
        
        except ValueError:
            print("Por favor, introduce valores numéricos válidos.")
        
        # Preguntar si se desea realizar otra operación
        repetir = input("¿Quieres realizar otra operación? (s/n): ").strip().lower()
        if repetir != 's':
            print("¡Gracias por usar la calculadora!")
            break


