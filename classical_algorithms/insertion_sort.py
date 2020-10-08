def insertion_sort(array):
    n = len(array)
    # iterate over unsorted array, first element is always sorted
    for unsorted_index in range(1,n): 
        # unsorted value is
        unsorted_value = array[unsorted_index] 
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
    return array

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6] 
    sorted_array = insertion_sort(array)
    print(sorted_array)
