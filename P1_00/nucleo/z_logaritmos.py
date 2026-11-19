import math

class Logaritmos:
    
    def logaritmo(self, numero):
        if numero <= 0:
            raise ValueError(
                "El logaritmo requiere un número mayor que cero."
            )

        return math.log10(numero)

    def logaritmo_natural(self, numero):
        if numero <= 0:
            raise ValueError(
                "El logaritmo natural requiere un número mayor que cero."
            )

        return math.log(numero)

    def logaritmo_base(self, numero, base):
        if numero <= 0:
            raise ValueError(
                "El argumento debe ser mayor que cero."
            )

        if base <= 0 or base == 1:
            raise ValueError(
                "La base debe ser mayor que cero y diferente de uno."
            )

        return math.log(numero, base)

    def exponencial(self, numero):
        return math.exp(numero)

    def potencia_diez(self, numero):
        return 10 ** numero
