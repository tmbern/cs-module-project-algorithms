'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # single_number = []
    # for i in arr:
    #     if i in single_number:
    #         single_number.remove(i)
    #     else:
    #         single_number.append(i)
    # return single_number[0]

    for i in arr:
        if arr.count(arr[i]) == 1:
            return arr[i]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")