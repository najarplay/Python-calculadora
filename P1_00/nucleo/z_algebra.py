
import math


class Algebra:

    # POTENCIAS

    def potencia(self, base, exponente):
        return base ** exponente

    def cuadrado(self, numero):
        return numero ** 2

    def cubo(self, numero):
        return numero ** 3

    # RAICES

    def raiz_cuadrada(self, numero):
        if numero < 0:
            raise ValueError(
                "No se puede calcular la raíz cuadrada "
                "de un número negativo en los números reales."
            )

        return math.sqrt(numero)

    def raiz_cubica(self, numero):
        if numero < 0:
            return -(abs(numero) ** (1 / 3))

        return numero ** (1 / 3)

    def raiz_n(self, numero, indice):
        if indice == 0:
            raise ValueError("El índice de la raíz no puede ser cero.")

        if numero < 0 and indice % 2 == 0:
            raise ValueError(
                "No existe una raíz real de índice par "
                "para un número negativo."
            )

        if numero < 0:
            return -(abs(numero) ** (1 / indice))

        return numero ** (1 / indice)

    # INVERSOS

    def inverso(self, numero):
        if numero == 0:
            raise ZeroDivisionError(
                "No existe el inverso de cero."
            )

        return 1 / numero

    # VALOR ABSOLUTO

    def valor_absoluto(self, numero):
        return abs(numero)

    # REDONDEO

    def redondear(self, numero, decimales=2):
        return round(numero, decimales)

    def truncar(self, numero, decimales=0):
        factor = 10 ** decimales
        return math.trunc(numero * factor) / factor

    def techo(self, numero):
        return math.ceil(numero)

    def piso(self, numero):
        return math.floor(numero)
