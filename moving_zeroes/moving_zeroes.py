'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    new_arr = []
    for i in arr:
        if i != 0:
            new_arr.insert(0, i)
        else:
            new_arr.append(i)
    return new_arr

    # could also try to remove 0 and append 0 for however many
    # times there are 0 in the list. 

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")