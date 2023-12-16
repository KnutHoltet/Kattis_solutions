def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1][:2] > arr[j][:2]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def printList(arr, tall):
    n = len(arr)
    for i in range(n):
        print(arr[i])

    if tall > 0:

        print()



ant_input = int(input())

while ant_input > 0:
    arr = []
    for i in range(ant_input):
        arr.append(input())
    
    ant_input = int(input())
    
    selectionSort(arr)
    printList(arr, ant_input)

