"""
    VARUN KUMAR
    https://www.hackerrank.com/challenges/python-string-formatting/problem
"""


def print_formatted(number):
    # your code goes here
    bin_width = len(bin(number)[1:])

    for i in range(1, number + 1):
        decimal = i
        octal = oct(i)[2:]
        hex_dec = hex(i).upper()[2:]
        binary = bin(i)[2:]
        print(f"{str(i).rjust(bin_width - 1, ' ')}{octal.rjust(bin_width, ' ')}{hex_dec.rjust(bin_width, ' ')}{binary.rjust(bin_width, ' ')}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
