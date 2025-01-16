"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module contains functions to calculate the preparation time, baking time,
and elapsed time required to cook a lasagna.
"""

EXPECTED_BAKE_TIME = 40  # This is the constant representing the expected bake time.
print(EXPECTED_BAKE_TIME)

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for lasagna layers.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes) for all layers.

    This function takes the number of layers and returns the time spent preparing the lasagna,
    where each layer takes 2 minutes to prepare.
    """
    # Each layer takes 2 minutes to prepare
    return 2 * number_of_layers
    
print(preparation_time_in_minutes(1))


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - the amount of time the lasagna has been baking.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    This function calculates how much longer the lasagna needs to bake based on the time already
    spent in the oven. It subtracts the elapsed bake time from the expected bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

elapsed_time = 30
print(bake_time_remaining(elapsed_time))


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time (preparation + baking).

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - the amount of time the lasagna has been baking.
    :return: int - total elapsed time (in minutes) including both preparation and baking.

    This function calculates the total elapsed time spent cooking the lasagna, which includes the time
    for preparing the layers and the time already spent baking.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time

print(elapsed_time_in_minutes(1, 30))
