"""
selection sort algorithm in python
"""
def selection_sort(array, verbose = False):
    verboseprint = print if verbose else lambda *a, **k: None
    verboseprint('array to be sorted is {}'.format(array))
    # loop through array
    for current_index, current_value in enumerate(array):
        verboseprint('sorting index {}'.format(current_index))
        # initialize min value and min index
        min_index = current_index
        min_value = current_value
        # find min element index
        for temp_index , temp_value in enumerate(array[current_index:],current_index):
            if min_value > temp_value:
                min_index, min_value = temp_index, temp_value
        # swap current element with min element
        array[current_index], array[min_index] = array[min_index], array[current_index]
        verboseprint('swapping indexes {} and {}'.\
            format(current_index,min_index))
    verboseprint('sorted array is {}'.format(array))
    return array

if __name__ == "__main__":
    array = [64, 25, 12, 22, 11] 
    selection_sort(array,verbose=True)

"""
output:
array to be sorted is [64, 25, 12, 22, 11]
sorting index 0
swapping indexes 0 and 4
sorting index 1
swapping indexes 1 and 2
sorting index 2
swapping indexes 2 and 3
sorting index 3
swapping indexes 3 and 3
sorting index 4
swapping indexes 4 and 4
sorted array is [11, 12, 22, 25, 64]
"""