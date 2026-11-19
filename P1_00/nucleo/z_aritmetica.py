
class Aritmetica:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError(
                "No se puede dividir entre cero."
            )
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError(
                "No se puede calcular el módulo entre cero."
            )
        return a % b

    def division_entera(self, a, b):
        if b == 0:
            raise ZeroDivisionError(
                "No se puede dividir entre cero."
            )
        return a // b
