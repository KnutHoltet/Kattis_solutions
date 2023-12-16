def backspace(string):
    arr = []
    skip = 0

    for s in reversed(string):
        if s == "<":
            skip += 1
        elif skip > 0:
            skip -= 1
        else:
            arr.append(s)

    return "".join(reversed(arr))


def main():
    string = input()
    print(backspace(string))

if __name__ == "__main__":
    main()

