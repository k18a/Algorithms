"""
given string s; 
repeat string until it reaches n elements;
count the number of 'a's
"""
def repeated_string(s, n):
    # find out the count
    count = (s.count("a") * (n // len(s)) + \
        s[:n % len(s)].count("a"))
    return count

if __name__ == '__main__':
    s = 'aba'
    count = repeated_string(s,10)
    print(count)