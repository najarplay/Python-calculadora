
class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b

    def potencia(self, a, b):
        return a ** b

def mostrar_menu():
    print("\n==============================")
    print("       CALCULADORA V01")
    print("==============================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("0. Salir")
    print("==============================")

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: introduce un número válido.")

def main():
    calculadora = Calculadora()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una operación: ")

        if opcion == "0":
            print("Cerrando calculadora...")
            break

        if opcion not in ("1", "2", "3", "4", "5"):
            print("Opción no válida.")
            continue

        numero1 = obtener_numero("Introduce el primer número: ")
        numero2 = obtener_numero("Introduce el segundo número: ")

        try:
            if opcion == "1":
                resultado = calculadora.sumar(numero1, numero2)
                operacion = "Suma"

            elif opcion == "2":
                resultado = calculadora.restar(numero1, numero2)
                operacion = "Resta"

            elif opcion == "3":
                resultado = calculadora.multiplicar(numero1, numero2)
                operacion = "Multiplicación"

            elif opcion == "4":
                resultado = calculadora.dividir(numero1, numero2)
                operacion = "División"

            elif opcion == "5":
                resultado = calculadora.potencia(numero1, numero2)
                operacion = "Potencia"

            print(f"\n{operacion}: {resultado:g}")

        except ZeroDivisionError as error:
            print(f"Error: {error}")



if __name__ == "__main__":
    main()
