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
        zeros = int(result[2]) * [0]
        zeros = "".join(str(x) for x in zeros)
        #print(zeros)
        result = "".join(result[0:2]) + str(zeros)
    final = obtener_prefijo_ohms(int(result))
    return final


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
        print(valor, "ohms" )
        return f"{int(valor)} ohms"

    # Calcula el exponente base 10 truncado a múltiplos de 3
    import math

    exponente = math.floor(math.log10(abs(valor)) / 3) * 3

    # Obtiene el prefijo o deja vacío si es menor a mil
    prefijo = prefijos.get(exponente, "")
    valor_reducido = valor / (10**exponente)
    #print(f"{int(valor_reducido)} {prefijo}ohms")
    return f"{int(valor_reducido)} {prefijo}ohms"

if __name__ == '__main__':
    label(["blue", "green", "yellow", "orange"])
    label(["black", "black", "black"])