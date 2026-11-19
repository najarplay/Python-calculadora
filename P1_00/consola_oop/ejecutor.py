class EjecutorOperaciones:

    def __init__(self, entrada):
        self.entrada = entrada

        # OPERACIONES DE LA CALCULADORA NORMAL
        self.operaciones_normales = {
            "2": ("sumar", ["numero", "numero"]),
            "3": ("restar", ["numero", "numero"]),
            "4": ("multiplicar", ["numero", "numero"]),
            "5": ("dividir", ["numero", "numero"]),
            "6": ("modulo", ["numero", "numero"]),
            "7": ("division_entera", ["numero", "numero"]),
        }

        # OPERACIONES DE LA CALCULADORA CIENTÍFICA
        self.operaciones_cientificas = {
            # ARITMÉTICA Y ÁLGEBRA
            "2": ("sumar", ["numero", "numero"]),
            "3": ("restar", ["numero", "numero"]),
            "4": ("multiplicar", ["numero", "numero"]),
            "5": ("dividir", ["numero", "numero"]),
            "6": ("modulo", ["numero", "numero"]),
            "7": ("division_entera", ["numero", "numero"]),
            "8": ("potencia", ["numero", "numero"]),
            "9": ("cuadrado", ["numero"]),
            "10": ("cubo", ["numero"]),
            "11": ("raiz_cuadrada", ["numero"]),
            "12": ("raiz_cubica", ["numero"]),
            "13": ("raiz_n", ["numero", "entero"]),
            "14": ("inverso", ["numero"]),
            "15": ("valor_absoluto", ["numero"]),
            "16": ("redondear", ["numero", "entero"]),
            "17": ("truncar", ["numero", "entero"]),
            "18": ("techo", ["numero"]),
            "19": ("piso", ["numero"]),

            # TRIGONOMETRÍA
            "20": ("seno", ["numero"]),
            "21": ("coseno", ["numero"]),
            "22": ("tangente", ["numero"]),
            "23": ("arcoseno", ["numero"]),
            "24": ("arcocoseno", ["numero"]),
            "25": ("arcotangente", ["numero"]),

            # LOGARITMOS
            "26": ("logaritmo", ["numero"]),
            "27": ("logaritmo_natural", ["numero"]),
            "28": ("logaritmo_base", ["numero", "numero"]),
            "29": ("exponencial", ["numero"]),
            "30": ("potencia_diez", ["numero"]),

            # COMBINATORIA
            "31": ("factorial", ["entero"]),
            "32": ("permutaciones", ["entero", "entero"]),
            "33": ("combinaciones", ["entero", "entero"]),

            # CONSTANTES
            "34": ("pi", []),
            "35": ("euler", []),

            # ESTADÍSTICA
            "36": ("media", ["lista"]),
            "37": ("mediana", ["lista"]),
            "38": ("moda", ["lista"]),
            "39": ("varianza_poblacional", ["lista"]),
            "40": ("varianza_muestral", ["lista"]),
            "41": ("desviacion_estandar_poblacional", ["lista"]),
            "42": ("desviacion_estandar_muestral", ["lista"]),
            "43": ("sumatoria", ["lista"]),

            # CONVERSIONES ANGULARES
            "44": ("grados_a_radianes", ["numero"]),
            "45": ("radianes_a_grados", ["numero"]),
            "46": ("grados_a_gradianes", ["numero"]),
            "47": ("gradianes_a_grados", ["numero"]),
            "48": ("radianes_a_gradianes", ["numero"]),
            "49": ("gradianes_a_radianes", ["numero"]),

            # ALEATORIOS
            "50": ("aleatorio", []),
            "51": ("aleatorio_entero", ["entero", "entero"]),
        }

    def obtener_argumentos(self, tipos):
        argumentos = []

        for tipo in tipos:

            if tipo == "numero":
                valor = self.entrada.obtener_numero(
                    "Introduce un número: "
                )

            elif tipo == "entero":
                valor = self.entrada.obtener_entero(
                    "Introduce un número entero: "
                )

            elif tipo == "lista":
                valor = self.entrada.obtener_lista(
                    "Introduce los números separados por comas: "
                )

            argumentos.append(valor)

        return argumentos

    def ejecutar(self, calculadora, opcion, cientifica=False):
        operaciones = (
            self.operaciones_cientificas
            if cientifica
            else self.operaciones_normales
        )

        if opcion not in operaciones:
            raise ValueError("La opción seleccionada no es válida.")

        metodo, tipos_argumentos = operaciones[opcion]

        argumentos = self.obtener_argumentos(tipos_argumentos)

        operacion = getattr(calculadora, metodo)

        return operacion(*argumentos)
