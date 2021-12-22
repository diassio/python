#task2
arr = []
n = int(input("Enter number of elements in your array : "))
for i in range(0, n):
    element = int(input())
    arr.append(element)
print('your array is: {0}'.format(arr))
for i in range(0, len(arr) -1, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
print('your modified array is {0}'.format(arr))