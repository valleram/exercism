def recite(start_verse, end_verse):
    # 1. Almacenamos las partes de la rima en orden de aparición
    # Cada elemento contiene el sujeto de ese verso y la acción que conecta con el anterior
    parts = [
        ("the house that Jack built.", ""),
        ("the malt", "that lay in "),
        ("the rat", "that ate "),
        ("the cat", "that killed "),
        ("the dog", "that worried "),
        ("the cow with the crumpled horn", "that tossed "),
        ("the maiden all forlorn", "that milked "),
        ("the man all tattered and torn", "that kissed "),
        ("the priest all shaven and shorn", "that married "),
        ("the rooster that crowed in the morn", "that woke "),
        ("the farmer sowing his corn", "that kept "),
        ("the horse and the hound and the horn", "that belonged to ")
    ]

    verses = []

    # 2. Iteramos desde el verso inicial hasta el final
    for verse_num in range(start_verse, end_verse + 1):
        # El verso siempre empieza con "This is "
        current_verse = "This is "

        # 3. Construimos la cadena hacia atrás (acumulativa)
        # Recorremos la lista al revés desde el índice del verso actual hasta 0
        for i in range(verse_num - 1, -1, -1):
            subject, action = parts[i]

            if i == verse_num - 1:
                # Si es el primer elemento del verso actual, solo añadimos el sujeto
                current_verse += f"{subject} "
            else:
                # Para los siguientes, conectamos la acción anterior con el nuevo sujeto
                prev_action = parts[i + 1][1]
                current_verse += f"{prev_action}{subject} "

        # Limpiamos espacios adicionales al final y guardamos el verso
        verses.append(current_verse.strip())
    print(verses)
    return verses

if __name__ == "__main__":
    recite(8, 8),