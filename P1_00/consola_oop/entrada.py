class EntradaConsola:
    """
    Gestiona la captura y validación de datos
    introducidos por el usuario en la terminal.
    Método	            Función
    obtener_opcion()	Recibe opciones de los menús.
    obtener_numero()	Recibe números enteros o decimales.
    obtener_entero()	Recibe exclusivamente números enteros.
    obtener_lista()	    Recibe varios números separados por comas.
    """

    def obtener_opcion(self, mensaje="Selecciona una opción: "):
        return input(mensaje).strip()

    def obtener_numero(self, mensaje="Introduce un número: "):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: introduce un número válido.")

    def obtener_entero(self, mensaje="Introduce un entero: "):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: introduce un número entero válido.")

    def obtener_lista(self, mensaje="Introduce los números separados por comas: "):
        while True:
            try:
                entrada = input(mensaje)
                datos = [float(numero.strip()) for numero in entrada.split(",")]

                if not datos:
                    raise ValueError

                return datos

            except ValueError:
                print("Error: introduce números separados por comas.")
