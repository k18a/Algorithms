"""
merge sort
"""
def merge_sort(array, verbose=False): 
    verboseprint = print if verbose else lambda *a, **k: None
    n = len(array)
    # sort array if length is greater than 1
    if len(array)>1: 
        verboseprint('sorting array {}'.format(array))
        
        # get left and right arrays
        mid_point = len(array)//2
        left_array = array[:mid_point] 
        right_array = array[mid_point:] 

        # recursively sort left and right arrays
        left_array = merge_sort(left_array,verbose) 
        right_array = merge_sort(right_array,verbose) 

        # initialize sorted array
        sorted_array = [] 

        # merge left and right array into sorted array
        while left_array and right_array: 
            if left_array[0]<right_array[0]: 
                sorted_array.append(left_array.pop(0)) 
            else: 
                sorted_array.append(right_array.pop(0)) 
        # add all remaining elements
        sorted_array.extend(left_array)
        sorted_array.extend(right_array)
        verboseprint('sorted array {}'.format(sorted_array))
    else:
        # return single element
        sorted_array = array
    return sorted_array 

if __name__ == "__main__":
    array = [12,44,235,234,23,522,520]
    merge_sort(array, verbose=True)
    
"""
output:
sorting array [12, 44, 235, 234, 23, 522, 520]
sorting array [12, 44, 235]
sorting array [44, 235]
sorted array [44, 235]
sorted array [12, 44, 235]
sorting array [234, 23, 522, 520]
sorting array [234, 23]
sorted array [23, 234]
sorting array [522, 520]
sorted array [520, 522]
sorted array [23, 234, 520, 522]
sorted array [12, 23, 44, 234, 235, 520, 522]
"""
