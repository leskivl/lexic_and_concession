# find max indices of values
# using list comprehension
def find_max(array):
    max_value = max(array)
    indicies = [index for index, value in enumerate(array) if value == max_value]
    return indicies


# replace of non-maximum values to number -1
def replace_nonmax_to_neg_1(array, max_indices):
    for index in range(len(array)):
        if index not in max_indices:
            array[index] = -1
    return array
