"""
shell sort
"""
def shell_sort(array, insertion=False, verbose=False):
    verboseprint = print if verbose else lambda *a, **k: None
    verboseprint('array to be sorted is {}'.format(array))

    # define window
    if insertion:
        window = 1
    else:
        window = len(array)//2

    # loop for different windows
    while window >= 1:
        verboseprint('\nshell sort with window {}'.format(window))
        # move through unsorted array
        for unsorted_index, unsorted_value in enumerate(array[window:],window):
            verboseprint('sorting {} at index {}'.\
                format(unsorted_value, unsorted_index))
            # initialize sorted index and value
            sorted_index = unsorted_index - window
            sorted_value = array[sorted_index]
            # compare and loop through sorted value 
            while unsorted_value < sorted_value and sorted_index >= 0:
                # move sorted value 
                array[sorted_index+window] = sorted_value
                verboseprint('moving index {} to {}'\
                    .format(sorted_index, sorted_index+window))
                # re initialize sorted index and value for next loop
                sorted_index -= window
                sorted_value = array[sorted_index]
            # move unsorted value
            array[sorted_index+window] = unsorted_value
            verboseprint('moving {} at index {} to index {}'.\
                format(unsorted_value,unsorted_index,sorted_index+window))
            verboseprint('array is now {}'.format(array))
        # decrease window by half
        window //= 2
    verboseprint('sorted array is {}'.format(array))
    return array

if __name__ == "__main__":
    array = [12,42,234,4,2,512]
    shell_sort(array,insertion=False,verbose=True)

"""
output:
array to be sorted is [12, 42, 234, 4, 2, 512]

shell sort with window 3
sorting 4 at index 3
moving index 0 to 3
moving 4 at index 3 to index 0
array is now [4, 42, 234, 12, 2, 512]
sorting 2 at index 4
moving index 1 to 4
moving 2 at index 4 to index 1
array is now [4, 2, 234, 12, 42, 512]
sorting 512 at index 5
moving 512 at index 5 to index 5
array is now [4, 2, 234, 12, 42, 512]

shell sort with window 1
sorting 2 at index 1
moving index 0 to 1
moving 2 at index 1 to index 0
array is now [2, 4, 234, 12, 42, 512]
sorting 234 at index 2
moving 234 at index 2 to index 2
array is now [2, 4, 234, 12, 42, 512]
sorting 12 at index 3
moving index 2 to 3
moving 12 at index 3 to index 2
array is now [2, 4, 12, 234, 42, 512]
sorting 42 at index 4
moving index 3 to 4
moving 42 at index 4 to index 3
array is now [2, 4, 12, 42, 234, 512]
sorting 512 at index 5
moving 512 at index 5 to index 5
array is now [2, 4, 12, 42, 234, 512]
sorted array is [2, 4, 12, 42, 234, 512]
"""