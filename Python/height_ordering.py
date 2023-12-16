def insertionSort(arr):
    n = len(arr)
    teller = 0
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
            teller += 1
    
    return str(teller)


antall_linjer = int(input())

for i in range(antall_linjer):
    input_line = input().strip()

    numbers = list(map(int, input_line.split()))

    dataset_number = numbers[0]

    heights = numbers[1:]

    print(f"{dataset_number} " + insertionSort(heights))

