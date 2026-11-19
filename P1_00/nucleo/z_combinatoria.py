import math


class Combinatoria:
    
    def factorial(self, numero):
        if not isinstance(numero, int) or isinstance(numero, bool):
            raise TypeError("El factorial requiere un número entero.")

        if numero < 0:
            raise ValueError(
                "El factorial no admite números negativos."
            )

        return math.factorial(numero)

    def permutaciones(self, n, r):
        self._validar_parametros(n, r)

        return math.perm(n, r)

    def combinaciones(self, n, r):
        self._validar_parametros(n, r)

        return math.comb(n, r)

    def _validar_parametros(self, n, r):
        for nombre, valor in (("n", n), ("r", r)):
            if not isinstance(valor, int) or isinstance(valor, bool):
                raise TypeError(
                    f"El parámetro {nombre} debe ser un entero."
                )

        if n < 0 or r < 0:
            raise ValueError(
                "Los parámetros no pueden ser negativos."
            )

        if r > n:
            raise ValueError(
                "El segundo parámetro no puede ser mayor que el primero."
            )
