"""
Function to calculate fibonaci number using a recursive technique. 
Fibonaci number is given as:
\(F(n) = F(n-1) + F(n-2)\)
"""
# initialize base case for 0 and 1 with memoization
memo = {0:0,1:1}

def fibonaci_recursive(n):
    # if value is not in memo
    if n not in memo:
        # fibonaci number is given as
        memo[n] = fibonaci_recursive(n-1) + fibonaci_recursive(n-2)
    return memo[n]

if __name__ == "__main__":
    print(fibonaci_recursive(15))