"""
Help you cook a gorgeous lasagna from your favorite cookbook.
"""
EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time per layer.

        :param number_of_layers: int baking time already elapsed.
        :return: int minutes needed to make those layers.

        Function that takes the number of layers you want to add to the lasagna as
        an argument and returns how many minutes you would spend making them.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate preparation time per layer.

            :param number_of_layers: int baking time already elapsed.
            :param elapsed_bake_time: int number of minutes the lasagna has been baking in the oven.
            :return: int total number of minutes you've been cooking.

            This function should return the total number of minutes you've been cooking,
            or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time
