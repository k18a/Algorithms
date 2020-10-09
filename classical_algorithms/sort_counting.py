"""
counting sort
"""
def counting_sort(input_array, inplace = True, exponent = 1):
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

    # loop through input array in reverse to populate output array
    for input_index in reversed(range(n)):
        # get count index of input element
        count_index = int((input_array[input_index]/exponent)%10)
        # get output index from count array
        # subtract 1 as python is 0 indexed 
        output_index = count_array[count_index] - 1 
        # place input element in output array
        output_array[output_index] = input_array[input_index]
        # decrement value in count array
        count_array[count_index] -= 1
    
    if inplace:
        input_array[:] = output_array[:]
        return 
    else:
        return output_array

if __name__ == "__main__":
    array = [1,2,3,4,1,2,3,4,1,2,3]
    sorted_array = counting_sort(array,inplace=False)
    print(sorted_array)