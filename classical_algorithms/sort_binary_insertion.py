"""
binary insertion sort
"""
import bisect

def binary_insertion_sort(array, verbose = False):
    # define verboseprint
    verboseprint = print if verbose else lambda *a, **k: None
    # loop through unsorted array, first element is already sorted
    verboseprint('array to be sorted is {}'.format(array))
    for unsorted_index, unsorted_value in enumerate(array[1:],1):
        # get sorted index using binary search
        sorted_index = bisect.bisect_right(\
            array,unsorted_value,0,unsorted_index-1)
        verboseprint('{} at index {} needs to be at {}'.\
            format(unsorted_value,unsorted_index,sorted_index))
        # array is given as
        array = array[:sorted_index]+\
            [unsorted_value]+\
                array[sorted_index:unsorted_index]+\
                    array[unsorted_index+1:]
        verboseprint('array after {} insertions is {}'.\
            format(unsorted_index,array))
    return array

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6] 
    binary_insertion_sort(array,verbose=True)

"""
output:
array to be sorted is [12, 11, 13, 5, 6]
11 at index 1 needs to be at 0
array after 1 insertions is [11, 12, 13, 5, 6]
13 at index 2 needs to be at 1
array after 2 insertions is [11, 13, 12, 5, 6]
5 at index 3 needs to be at 0
array after 3 insertions is [5, 11, 13, 12, 6]
6 at index 4 needs to be at 1
array after 4 insertions is [5, 6, 11, 13, 12]
"""