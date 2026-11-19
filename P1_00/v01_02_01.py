# dorecion  ...\app-python\calculadora>
# comando   python -m P1_00.consola

from calculadora.P1_00.nucleo import Calculadora, CalculadoraCientifica


# ==================================================
# 1. MENÚ PRINCIPAL
# ==================================================

def menu_principal():
    print("\n" + "=" * 42)
    print("              CALCULADORA")
    print("=" * 42)
    print("1. Calculadora normal")
    print("2. Calculadora científica")
    print("0. Salir")
    print("=" * 42)

    return input("¿Qué calculadora deseas utilizar?: ").strip()


# ==================================================
# 2. MENÚ CALCULADORA NORMAL
# ==================================================

def menu_normal():
    print("\n" + "=" * 42)
    print("          CALCULADORA NORMAL")
    print("=" * 42)

    print("\nOPERACIONES BÁSICAS")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Módulo")
    print("7. División entera")

    print("\n1. Cambiar calculadora")
    print("0. Salir")
    print("=" * 42)

    return input("Selecciona una operación: ").strip()


# ==================================================
# 3. MENÚ CALCULADORA CIENTÍFICA
# ==================================================

def menu_cientifica():
    print("\n" + "=" * 42)
    print("        CALCULADORA CIENTÍFICA")
    print("=" * 42)

    print("\nOPERACIONES BÁSICAS")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Módulo")
    print("7. División entera")

    print("\nÁLGEBRA")
    print("8. Potencia")
    print("9. Cuadrado")
    print("10. Cubo")
    print("11. Raíz cuadrada")
    print("12. Raíz cúbica")
    print("13. Raíz n")
    print("14. Inverso")
    print("15. Valor absoluto")
    print("16. Redondear")
    print("17. Truncar")
    print("18. Techo")
    print("19. Piso")

    print("\nTRIGONOMETRÍA")
    print("20. Seno")
    print("21. Coseno")
    print("22. Tangente")
    print("23. Arcoseno")
    print("24. Arcocoseno")
    print("25. Arcotangente")

    print("\nLOGARITMOS")
    print("26. Logaritmo base 10")
    print("27. Logaritmo natural")
    print("28. Logaritmo de base n")
    print("29. Exponencial")
    print("30. Potencia de 10")

    print("\nCOMBINATORIA")
    print("31. Factorial")
    print("32. Permutaciones")
    print("33. Combinaciones")

    print("\nCONSTANTES")
    print("34. Pi")
    print("35. Euler")

    print("\nESTADÍSTICA")
    print("36. Media")
    print("37. Mediana")
    print("38. Moda")
    print("39. Varianza poblacional")
    print("40. Varianza muestral")
    print("41. Desviación estándar poblacional")
    print("42. Desviación estándar muestral")
    print("43. Sumatoria")

    print("\nCONVERSIONES ANGULARES")
    print("44. Grados a radianes")
    print("45. Radianes a grados")
    print("46. Grados a gradianes")
    print("47. Gradianes a grados")
    print("48. Radianes a gradianes")
    print("49. Gradianes a radianes")

    print("\nNÚMEROS ALEATORIOS")
    print("50. Número aleatorio")
    print("51. Número entero aleatorio")

    print("\n1. Cambiar calculadora")
    print("0. Salir")
    print("=" * 42)

    return input("Selecciona una operación: ").strip()


# ==================================================
# 4. ENTRADA Y VALIDACIÓN DE DATOS
# ==================================================

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: introduce un número válido.")


def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero.")


def obtener_lista(mensaje):
    while True:
        try:
            entrada = input(mensaje)
            datos = [float(valor.strip()) for valor in entrada.split(",")]

            if not datos:
                raise ValueError

            return datos

        except ValueError:
            print("Introduce números separados por comas.")
            print("Ejemplo: 2, 4, 6, 8")


# ==================================================
# 5. CATÁLOGO DE OPERACIONES
# ==================================================

# Cada operación contiene:
# nombre, método y parámetros de entrada.
#
# Tipo de entrada:
# numero = decimal o entero
# entero = número entero
# lista = colección de números

OPERACIONES = {

    # OPERACIONES BÁSICAS
    "2": ("Suma", "sumar", [
        ("Primer número: ", "numero"),
        ("Segundo número: ", "numero")
    ]),
    "3": ("Resta", "restar", [
        ("Primer número: ", "numero"),
        ("Segundo número: ", "numero")
    ]),
    "4": ("Multiplicación", "multiplicar", [
        ("Primer número: ", "numero"),
        ("Segundo número: ", "numero")
    ]),
    "5": ("División", "dividir", [
        ("Primer número: ", "numero"),
        ("Segundo número: ", "numero")
    ]),
    "6": ("Módulo", "modulo", [
        ("Primer número: ", "numero"),
        ("Segundo número: ", "numero")
    ]),
    "7": ("División entera", "division_entera", [
        ("Primer número: ", "numero"),
        ("Segundo número: ", "numero")
    ]),

    # ÁLGEBRA
    "8": ("Potencia", "potencia", [
        ("Base: ", "numero"),
        ("Exponente: ", "numero")
    ]),
    "9": ("Cuadrado", "cuadrado", [
        ("Número: ", "numero")
    ]),
    "10": ("Cubo", "cubo", [
        ("Número: ", "numero")
    ]),
    "11": ("Raíz cuadrada", "raiz_cuadrada", [
        ("Número: ", "numero")
    ]),
    "12": ("Raíz cúbica", "raiz_cubica", [
        ("Número: ", "numero")
    ]),
    "13": ("Raíz n", "raiz_n", [
        ("Radicando: ", "numero"),
        ("Índice: ", "entero")
    ]),
    "14": ("Inverso", "inverso", [
        ("Número: ", "numero")
    ]),
    "15": ("Valor absoluto", "valor_absoluto", [
        ("Número: ", "numero")
    ]),
    "16": ("Redondear", "redondear", [
        ("Número: ", "numero"),
        ("Cantidad de decimales: ", "entero")
    ]),
    "17": ("Truncar", "truncar", [
        ("Número: ", "numero"),
        ("Cantidad de decimales: ", "entero")
    ]),
    "18": ("Techo", "techo", [
        ("Número: ", "numero")
    ]),
    "19": ("Piso", "piso", [
        ("Número: ", "numero")
    ]),

    # TRIGONOMETRÍA
    "20": ("Seno", "seno", [
        ("Ángulo: ", "numero")
    ]),
    "21": ("Coseno", "coseno", [
        ("Ángulo: ", "numero")
    ]),
    "22": ("Tangente", "tangente", [
        ("Ángulo: ", "numero")
    ]),
    "23": ("Arcoseno", "arcoseno", [
        ("Número entre -1 y 1: ", "numero")
    ]),
    "24": ("Arcocoseno", "arcocoseno", [
        ("Número entre -1 y 1: ", "numero")
    ]),
    "25": ("Arcotangente", "arcotangente", [
        ("Número: ", "numero")
    ]),

    # LOGARITMOS
    "26": ("Logaritmo base 10", "logaritmo", [
        ("Número: ", "numero")
    ]),
    "27": ("Logaritmo natural", "logaritmo_natural", [
        ("Número: ", "numero")
    ]),
    "28": ("Logaritmo de base n", "logaritmo_base", [
        ("Número: ", "numero"),
        ("Base: ", "numero")
    ]),
    "29": ("Exponencial", "exponencial", [
        ("Exponente: ", "numero")
    ]),
    "30": ("Potencia de 10", "potencia_diez", [
        ("Exponente: ", "numero")
    ]),

    # COMBINATORIA
    "31": ("Factorial", "factorial", [
        ("Número entero: ", "entero")
    ]),
    "32": ("Permutaciones", "permutaciones", [
        ("n: ", "entero"),
        ("r: ", "entero")
    ]),
    "33": ("Combinaciones", "combinaciones", [
        ("n: ", "entero"),
        ("r: ", "entero")
    ]),

    # CONSTANTES
    "34": ("Pi", "pi", []),
    "35": ("Euler", "euler", []),

    # ESTADÍSTICA
    "36": ("Media", "media", [
        ("Datos separados por comas: ", "lista")
    ]),
    "37": ("Mediana", "mediana", [
        ("Datos separados por comas: ", "lista")
    ]),
    "38": ("Moda", "moda", [
        ("Datos separados por comas: ", "lista")
    ]),
    "39": ("Varianza poblacional", "varianza_poblacional", [
        ("Datos separados por comas: ", "lista")
    ]),
    "40": ("Varianza muestral", "varianza_muestral", [
        ("Datos separados por comas: ", "lista")
    ]),
    "41": ("Desviación estándar poblacional",
           "desviacion_estandar_poblacional", [
               ("Datos separados por comas: ", "lista")
           ]),
    "42": ("Desviación estándar muestral",
           "desviacion_estandar_muestral", [
               ("Datos separados por comas: ", "lista")
           ]),
    "43": ("Sumatoria", "sumatoria", [
        ("Datos separados por comas: ", "lista")
    ]),

    # CONVERSIONES ANGULARES
    "44": ("Grados a radianes", "grados_a_radianes", [
        ("Grados: ", "numero")
    ]),
    "45": ("Radianes a grados", "radianes_a_grados", [
        ("Radianes: ", "numero")
    ]),
    "46": ("Grados a gradianes", "grados_a_gradianes", [
        ("Grados: ", "numero")
    ]),
    "47": ("Gradianes a grados", "gradianes_a_grados", [
        ("Gradianes: ", "numero")
    ]),
    "48": ("Radianes a gradianes", "radianes_a_gradianes", [
        ("Radianes: ", "numero")
    ]),
    "49": ("Gradianes a radianes", "gradianes_a_radianes", [
        ("Gradianes: ", "numero")
    ]),

    # ALEATORIOS
    "50": ("Número aleatorio", "aleatorio", []),
    "51": ("Número entero aleatorio", "aleatorio_entero", [
        ("Límite mínimo: ", "entero"),
        ("Límite máximo: ", "entero")
    ])
}


# ==================================================
# 6. EJECUTAR OPERACIONES
# ==================================================

def ejecutar_operacion(calculadora, opcion):

    if opcion not in OPERACIONES:
        print("\nOpción no válida.")
        return

    nombre, metodo, parametros = OPERACIONES[opcion]

    try:
        argumentos = []

        for mensaje, tipo in parametros:

            if tipo == "numero":
                valor = obtener_numero(mensaje)

            elif tipo == "entero":
                valor = obtener_entero(mensaje)

            elif tipo == "lista":
                valor = obtener_lista(mensaje)

            argumentos.append(valor)

        funcion = getattr(calculadora, metodo)
        resultado = funcion(*argumentos)

        print("\n" + "-" * 42)
        print(f"Operación: {nombre}")
        print(f"Resultado: {resultado}")
        print("-" * 42)

    except (ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
        print(f"\nError al realizar la operación: {error}")


# ==================================================
# 7. CONTROL DE LAS CALCULADORAS
# ==================================================

def iniciar_calculadora(calculadora, cientifica=False):

    while True:

        if cientifica:
            opcion = menu_cientifica()
        else:
            opcion = menu_normal()

        if opcion == "0":
            return "salir"

        if opcion == "1":
            return "cambiar"

        ejecutar_operacion(calculadora, opcion)


# ==================================================
# 8. CONTROL PRINCIPAL DEL PROGRAMA
# ==================================================

def main():

    calculadora_normal = Calculadora()
    calculadora_cientifica = CalculadoraCientifica()

    while True:

        opcion = menu_principal()

        if opcion == "0":
            print("\nCerrando calculadora...")
            break

        elif opcion == "1":
            resultado = iniciar_calculadora(calculadora_normal)

        elif opcion == "2":
            resultado = iniciar_calculadora(
                calculadora_cientifica,
                cientifica=True
            )

        else:
            print("\nOpción no válida.")
            continue

        if resultado == "salir":
            print("\nCerrando calculadora...")
            break


# ==================================================
# 9. PUNTO DE EJECUCIÓN
# ==================================================

if __name__ == "__main__":
    main()
