"""
selection sort algorithm in python
"""
def selection_sort(array):
    # loop through array
    for current_index, current_value in enumerate(array):
        # initialize index of min value
        min_index = current_index
        # find min element index
        for temp_index , temp_value in enumerate(array[current_index:]):
            if current_value > temp_value:
                min_index = temp_index
        # swap current element with min element
        array[current_index], array[min_index] = array[min_index], array[current_index]
    return array

if __name__ == "__main__":
    A = [64, 25, 12, 22, 11] 
    sorted_array = selection_sort(A)
    print(sorted_array)