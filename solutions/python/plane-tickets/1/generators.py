"""Functions to automate Conda airlines ticketing system."""
import string
from itertools import islice
from lib2to3.pgen2.token import NUMBER


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = string.ascii_uppercase

    for i in range(number):
        yield letters[i % 4]




def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    asientos_generados = 0
    fila = 1
    letras = "ABCD"

    while asientos_generados < number:
        # Saltar la fila 13
        if fila == 13:
            fila += 1
            continue

        for letra in letras:
            if asientos_generados < number:
                yield f"{fila}{letra}"
                asientos_generados += 1
            else:
                return

        fila += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return dict(zip(passengers, generate_seats(len(passengers))))



def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        # Concatenamos el asiento con el ID del vuelo
        base_code = f"{seat}{flight_id}"

        # Rellenamos con '0' a la derecha hasta completar 12 caracteres
        yield base_code.ljust(12, '0')

if __name__ == '__main__':
    generate_seat_letters(7)