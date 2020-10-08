"""
Function to calculate fibonaci number using a recursive technique. 
Fibonaci number is given as:
\(F(n) = F(n-1) + F(n-2)\)
"""
def fibonaci_iterative(n):
    # initialize first 2 numbers
    previous_number, current_number = 0, 1
    # iterate n times
    for _ in range(1,n):
        ' fibonaci number is given as'
        previous_number, current_number = \
            current_number, previous_number + current_number
    return current_number

if __name__ == "__main__":
    print(fibonaci_iterative(15))