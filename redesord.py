def interc(arr, ori, des):
    if arr[ori] > arr[des]:
        arr[ori], arr[des] = arr[des], arr[ori]

def ordenar(arr):
    interc(arr, 0, 2)
    interc(arr, 1, 3)
    interc(arr, 0, 1)
    interc(arr, 2, 3)
    interc(arr, 1, 2)

arr = [2,3,4,1]

ordenar(arr)

print(arr)
    