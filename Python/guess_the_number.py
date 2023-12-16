arr = []
for i in range(1, 1001):
    arr.append(i)


low = 0
high = len(arr)


while low <= high:
    mid = (high + low) // 2

    print(arr[mid])
    guess = input()

    if guess == "correct":
        exit()

    elif guess == "higher":
        low = mid + 1

    else:
        high = mid - 1

