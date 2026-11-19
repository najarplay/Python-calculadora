
import random


class Aleatorios:
    
    def aleatorio(self):
        return random.random()

    def aleatorio_entero(self, minimo, maximo):
        if not isinstance(minimo, int) or isinstance(minimo, bool):
            raise TypeError("El límite mínimo debe ser un entero.")

        if not isinstance(maximo, int) or isinstance(maximo, bool):
            raise TypeError("El límite máximo debe ser un entero.")

        if minimo > maximo:
            raise ValueError(
                "El límite mínimo no puede ser mayor que el máximo."
            )

        return random.randint(minimo, maximo)
