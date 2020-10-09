"""
insertion sort
"""

def insertion_sort(array, verbose=False):
    # define verboseprint function
    verboseprint = print if verbose else lambda *a, **k: None
    # iterate over unsorted array, first element is always sorted
    verboseprint('array to be sorted is {}'.format(array))
    for unsorted_index, unsorted_value in enumerate(array[1:],1): 
        verboseprint('currently sorting {} at index {}'.format(unsorted_value, unsorted_index))
        # initialize sorted index and value at 1 less than unsorted
        sorted_index = unsorted_index-1
        sorted_value = array[sorted_index]
        # reverse loop through sorted array until value less than unsorted value is found
        while sorted_index >= 0 and unsorted_value < sorted_value : 
                # move value greater than unsorted value by 1 to the right
                array[sorted_index + 1] = array[sorted_index] 
                sorted_index -= 1
        # place unsorted value in the sorted array
        array[sorted_index + 1] = unsorted_value
        verboseprint('array after {} insertions is {}'.format(unsorted_index, array))
    return array

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6] 
    insertion_sort(array, verbose=True)