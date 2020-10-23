"""
counting sort
"""
def counting_sort(input_array, inplace = True, exponent = 1, verbose = False):
    verboseprint = print if verbose else lambda *a, **k: None
    verboseprint('array to be sorted is {}'.format(input_array))
    # length of input array
    n = len(input_array)
    # initialize output array
    output_array = [0]*n
    # initialize count array
    count_array = [0]*10 

    # loop through input array
    for input_index, input_value in enumerate(input_array):
        # get count_index
        count_index = int((input_value / exponent)%10)
        # populate count array
        count_array[count_index] += 1
    # cumulative sum of count array
    count_array = [sum(count_array[0:index+1]) for index in range(10)]
    verboseprint('count array for exponent {} is {}'.format(exponent,count_array))

    # loop through input array in reverse to populate output array
    for input_index in reversed(range(n)):
        # get count index of input element
        count_index = int((input_array[input_index]/exponent)%10)
        # get output index from count array
        # subtract 1 as python is 0 indexed 
        output_index = count_array[count_index] - 1 
        # place input element in output array
        verboseprint('index {} in input array goes to index {} in output array'.\
            format(input_index,output_index))
        output_array[output_index] = input_array[input_index]
        # decrement value in count array
        count_array[count_index] -= 1
    verboseprint('sorted array is {}'.format(output_array))

    if inplace:
        input_array[:] = output_array[:]
        return 
    else:
        return output_array

if __name__ == "__main__":
    array = [1,2,3,4,1,2,3,4,1,2,3]
    counting_sort(array,verbose=True)

"""
output:
array to be sorted is [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3]
count array for exponent 1 is [0, 3, 6, 9, 11, 11, 11, 11, 11, 11]
index 10 in input array goes to index 8 in output array
index 9 in input array goes to index 5 in output array
index 8 in input array goes to index 2 in output array
index 7 in input array goes to index 10 in output array
index 6 in input array goes to index 7 in output array
index 5 in input array goes to index 4 in output array
index 4 in input array goes to index 1 in output array
index 3 in input array goes to index 9 in output array
index 2 in input array goes to index 6 in output array
index 1 in input array goes to index 3 in output array
index 0 in input array goes to index 0 in output array
sorted array is [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
"""