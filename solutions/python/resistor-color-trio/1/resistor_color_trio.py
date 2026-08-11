COLORS_MAPPING: dict[str, int] = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors):
    """
    :param colors:
    :return:
    """
    result = [str(COLORS_MAPPING[item]) for item in colors if item in COLORS_MAPPING]
    if len(result) > 2:
        zeros_lst = list()
        for n in result[2:]:
            zeros = int(n) * [0]
            zeros_lst.append(zeros)
        resultado = "".join(
            str(numero) for sublista in zeros_lst for numero in sublista
        )
        result = "".join(result[0:2]) + str(resultado)
    obtener_prefijo_ohms(int(result))


def obtener_prefijo_ohms(valor):
    # Diccionario de prefijos (exponente : nombre)
    prefijos = {
        3: "kilo",
        6: "mega",
        9: "giga",
        12: "tera",
        15: "peta",
    }

    if valor == 0:
        return "ohms", valor

    # Calcula el exponente base 10 truncado a múltiplos de 3
    import math

    exponente = math.floor(math.log10(abs(valor)) / 3) * 3

    # Obtiene el prefijo o deja vacío si es menor a mil
    prefijo = prefijos.get(exponente, "")
    valor_reducido = valor / (10**exponente)
    return f"{int(valor_reducido)} {prefijo}ohms"
