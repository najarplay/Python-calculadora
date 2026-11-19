import math

from .z_tri_configuracion import ConfiguracionAngular as CA

class Trigonometria:
    
    def __init__(self, configuracion=None):
        self.configuracion_angular = (
            configuracion
            if configuracion is not None
            else CA()
        )

    # CONVERSIONES INTERNAS

    def _a_radianes(self, angulo):
        unidad = self.configuracion_angular.obtener_unidad_angular()

        if unidad == "DEG":
            return math.radians(angulo)

        if unidad == "GRAD":
            return angulo * math.pi / 200

        return angulo

    def _desde_radianes(self, angulo):
        unidad = self.configuracion_angular.obtener_unidad_angular()

        if unidad == "DEG":
            return math.degrees(angulo)

        if unidad == "GRAD":
            return angulo * 200 / math.pi

        return angulo

    # FUNCIONES TRIGONOMETRICAS DIRECTAS

    def seno(self, angulo):
        return math.sin(self._a_radianes(angulo))

    def coseno(self, angulo):
        return math.cos(self._a_radianes(angulo))

    def tangente(self, angulo):
        radianes = self._a_radianes(angulo)

        if math.isclose(math.cos(radianes), 0, abs_tol=1e-12):
            raise ValueError(
                "La tangente no está definida para este ángulo."
            )

        return math.tan(radianes)

    # FUNCIONES TRIGONOMETRICAS INVERSAS

    def arcoseno(self, numero):
        if not -1 <= numero <= 1:
            raise ValueError("El arcoseno requiere un valor entre -1 y 1.")

        resultado = math.asin(numero)
        return self._desde_radianes(resultado)

    def arcocoseno(self, numero):
        if not -1 <= numero <= 1:
            raise ValueError("El arcocoseno requiere un valor entre -1 y 1.")

        resultado = math.acos(numero)
        return self._desde_radianes(resultado)

    def arcotangente(self, numero):
        resultado = math.atan(numero)
        return self._desde_radianes(resultado)

    # FUNCIONES HIPERBOLICAS

    def seno_hiperbolico(self, numero):
        return math.sinh(numero)

    def coseno_hiperbolico(self, numero):
        return math.cosh(numero)

    def tangente_hiperbolica(self, numero):
        return math.tanh(numero)

    # FUNCIONES HIPERBOLICAS INVERSAS

    def arcoseno_hiperbolico(self, numero):
        return math.asinh(numero)

    def arcocoseno_hiperbolico(self, numero):
        if numero < 1:
            raise ValueError(
                "El arcocoseno hiperbólico requiere un valor mayor o igual a 1."
            )

        return math.acosh(numero)

    def arcotangente_hiperbolica(self, numero):
        if not -1 < numero < 1:
            raise ValueError(
                "El arcotangente hiperbólico requiere un valor entre -1 y 1."
            )

        return math.atanh(numero)
