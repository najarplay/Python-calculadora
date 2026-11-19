
class ConfiguracionAngular:
    
    UNIDADES_VALIDAS = ("DEG", "RAD", "GRAD")

    def __init__(self, unidad_angular="DEG"):
        self.establecer_unidad_angular(unidad_angular)

    def establecer_unidad_angular(self, unidad):
        unidad = unidad.upper()

        if unidad not in self.UNIDADES_VALIDAS:
            raise ValueError(
                "Unidad angular no válida. "
                "Utiliza DEG, RAD o GRAD."
            )

        self.unidad_angular = unidad

    def obtener_unidad_angular(self):
        return self.unidad_angular
