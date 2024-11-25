def find_missing_number(arr):

    missing_elements = []
    for ele in range(arr[0], arr[-1]+1):
        if ele not in arr:
            missing_elements.append(ele)
    print(missing_elements)

arr = [1,2,3,4,5,6,7,9,10]
find_missing_number(arr)