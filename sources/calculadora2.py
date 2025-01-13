import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz de un número negativo"
    return math.sqrt(a)

def modulo(a, b):
    return a % b

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def calculadora():
    operaciones = {
        '1': ('Suma', suma),
        '2': ('Resta', resta),
        '3': ('Multiplicación', multiplicacion),
        '4': ('División', division),
        '5': ('Potencia', potencia),
        '6': ('Raíz cuadrada', raiz_cuadrada),
        '7': ('Módulo', modulo),
    }

    while True:
        print("\nSeleccione una operación:")
        for key, (name, _) in operaciones.items():
            print(f"{key}. {name}")
        print("8. Salir")

        operacion = input("Ingrese el número de la operación: ")

        if operacion == '8':
            print("¡Gracias por usar la calculadora!")
            break

        if operacion in operaciones:
            if operacion == '6':  # Raíz cuadrada requiere solo un número
                num = obtener_numero("Ingrese el número: ")
                resultado = operaciones[operacion][1](num)
                print(f"Resultado: {resultado}")
            else:
                num1 = obtener_numero("Ingrese el primer número: ")
                num2 = obtener_numero("Ingrese el segundo número: ")
                resultado = operaciones[operacion][1](num1, num2)
                print(f"Resultado: {resultado}")
        else:
            print("Operación no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora()
