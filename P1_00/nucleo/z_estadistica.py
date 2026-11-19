import statistics


class Estadistica:
    
    def _validar_datos(self, datos):
        if not isinstance(datos, (list, tuple)):
            raise TypeError(
                "Los datos deben proporcionarse en una lista o tupla."
            )

        if not datos:
            raise ValueError("Se requiere al menos un dato.")

        for dato in datos:
            if isinstance(dato, bool) or not isinstance(dato, (int, float)):
                raise TypeError("Todos los datos deben ser números.")

    # MEDIDAS DE TENDENCIA CENTRAL
    def media(self, datos):
        self._validar_datos(datos)
        return statistics.mean(datos)

    def mediana(self, datos):
        self._validar_datos(datos)
        return statistics.median(datos)

    def moda(self, datos):
        self._validar_datos(datos)
        return statistics.multimode(datos)

    # MEDIDAS DE DISPERSIÓN
    def varianza_poblacional(self, datos):
        self._validar_datos(datos)
        return statistics.pvariance(datos)

    def varianza_muestral(self, datos):
        self._validar_datos(datos)
        return statistics.variance(datos)

    def desviacion_estandar_poblacional(self, datos):
        self._validar_datos(datos)
        return statistics.pstdev(datos)

    def desviacion_estandar_muestral(self, datos):
        self._validar_datos(datos)
        return statistics.stdev(datos)

    # SUMATORIA
    def sumatoria(self, datos):
        self._validar_datos(datos)
        return sum(datos)