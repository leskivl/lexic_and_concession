import numpy as np


def new_order_array(array, order):
    # function creates a new array in a certain order
    new_array = []
    for index in order:
        new_array.append(list(array[index - 1]))
    new_array = np.array(new_array)
    new_array = new_array.astype("float")
    return new_array


def find_indices_of_max_value(array):
    # function return index of max values
    max_value = np.nanmax(array)
    indices = [index for index, value in enumerate(array) if value == max_value]
    return indices


def replace_unnecessary_value(array, indices):
    # function that replace unnecessary value to null
    for index in range(len(array)):
        if index not in indices:
            array[index] = np.nan
    return array
