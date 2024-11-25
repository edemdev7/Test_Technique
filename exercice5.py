def custom_sort(arr):
    res = sorted(arr, key=str.lower)
    print(res)


a = ["Banana", "apple", "Cherry","zinc"]
custom_sort(a)