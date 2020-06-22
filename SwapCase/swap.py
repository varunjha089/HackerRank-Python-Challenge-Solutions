def swap_case(s):
    charList = []
    swapList = ''

    for char in s:
        charList.append(char)

    for case in charList:
        if case.isupper():
            toLower = case.lower()
            swapList += toLower
        else:
            toUpper = case.upper()
            swapList += toUpper
    return swapList


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
