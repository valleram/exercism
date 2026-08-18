COLORS = {
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

TOLERANCES = {
    "grey": "0.05",
    "violet": "0.1",
    "blue": "0.25",
    "green": "0.5",
    "brown": "1",
    "red": "2",
    "gold": "5",
    "silver": "10",
}


def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        first, second, multiplier, tolerance = colors
        significant_digits = COLORS[first] * 10 + COLORS[second]
    else:
        first, second, third, multiplier, tolerance = colors
        significant_digits = (
            COLORS[first] * 100
            + COLORS[second] * 10
            + COLORS[third]
        )

    resistance = significant_digits * 10 ** COLORS[multiplier]

    if resistance >= 1_000_000:
        value = resistance / 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        value = resistance / 1_000
        unit = "kiloohms"
    else:
        value = resistance
        unit = "ohms"

    # Evita mostrar .0 en valores enteros.
    value_text = f"{value:g}"

    return f"{value_text} {unit} ±{TOLERANCES[tolerance]}%"
if __name__ == '__main__':
    resistor_label(["orange", "orange", "black", "red"])
    resistor_label(["green", "brown", "orange", "grey"])
    resistor_label(["blue", "grey", "white", "brown", "brown"])
    resistor_label(["orange", "orange", "yellow", "black", "brown"])
    resistor_label(["violet", "orange", "red", "grey"])