
from .. import Calculadora, CalculadoraCientifica

from .entrada  import EntradaConsola
from .menu     import MenuConsola
from .ejecutor import EjecutorOperaciones


class AplicacionConsola:
    """
    Coordina los componentes de la aplicación
    de calculadora en terminal.
    """

    def __init__(self):
        # COMPONENTES DE LA INTERFAZ
        self.entrada = EntradaConsola()
        self.menu = MenuConsola()
        self.ejecutor = EjecutorOperaciones(self.entrada)

        # INSTANCIAS DE LAS CALCULADORAS
        self.calculadoras = {
            "1": (Calculadora(), False),
            "2": (CalculadoraCientifica(), True)
        }

    def iniciar(self):
        """
        Inicia el ciclo principal de la aplicación.
        """

        while True:
            self.menu.menu_principal()

            opcion = self.entrada.obtener_opcion()

            if opcion == "0":
                self.cerrar()
                break

            elif opcion in self.calculadoras:
                calculadora, cientifica = self.calculadoras[opcion]

                resultado = self.ejecutar_calculadora(
                    calculadora,
                    cientifica
                )

                if resultado == "salir":
                    self.cerrar()
                    break

            else:
                self.menu.mostrar_error(
                    "Selecciona una opción válida."
                )

    def ejecutar_calculadora(self, calculadora, cientifica):
        """
        Mantiene el ciclo de ejecución de cada calculadora.
        """

        while True:

            if cientifica:
                self.menu.menu_cientifica()
            else:
                self.menu.menu_normal()

            opcion = self.entrada.obtener_opcion()

            # SALIR DEL PROGRAMA
            if opcion == "0":
                return "salir"

            # REGRESAR AL MENÚ PRINCIPAL
            elif opcion == "1":
                return "cambiar"

            # EJECUTAR OPERACIÓN
            try:
                resultado = self.ejecutor.ejecutar(
                    calculadora,
                    opcion,
                    cientifica
                )

                self.menu.mostrar_resultado(resultado)

            except (ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
                self.menu.mostrar_error(str(error))

    def cerrar(self):
        """
        Muestra el mensaje de despedida.
        """

        print("\nCerrando calculadora...")
        print("Gracias por utilizar la aplicación.")
