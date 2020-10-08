# function to count number of words in file
def word_count(text_file):
    # initialize count dictionary
    count_dict = {}
    # iterate through text lines
    for line in text_file:
        # iterate through words
        words = line.split()
        for word in words:
            # add to dictionary
            if word not in count_dict:
                count_dict[word] = 1
            else:
                count_dict[word] += 1
    # return sorted dictionary with most repeated words first
    return sorted(count_dict.items(), key= lambda x: x[1], reverse= True)

if __name__ == '__main__':
    # open text file to perform search
    with open('test_cases/alice_in_wonderland.txt') as text_file:
        count_dict = word_count(text_file)
    print(count_dict)