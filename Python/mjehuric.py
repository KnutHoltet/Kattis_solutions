def bubbleSort(A):
    n = len(A)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1): 
            if A[j] > A[j + 1]:
                A[j], A[j +1] = A[j + 1], A[j]
                str_out = ""
                for i in range(len(A)):
                    str_out += str(A[i]) + " "
                print(str_out[:-1])
                



input_line = input().strip()
arr = list(map(int, input_line.split()))

bubbleSort(arr)
