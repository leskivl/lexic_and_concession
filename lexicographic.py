import numpy as np
import random

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

N = 5
num_criterion = 4
num_alternative = N + 3

# generating alternatives
alternative_array = np.array([random.randint(0, 5) for i in range(num_criterion * num_alternative)])
alternative_array = alternative_array.reshape(num_criterion, num_alternative)


first_order = [2, 1, 3, 4]
second_order = [4, 1, 2, 3]

# --------- lexicographic ordering ---------
print('\n\t\tТаблиця альтернатив \n', alternative_array)
print('\nПорядок сортування ', first_order)
alternative_1_order = new_order_array(alternative_array, first_order)
print('\n\t\tТаблиця нових альтернатив \n', alternative_array)
