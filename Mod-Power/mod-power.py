def pow_mod_pow(a, b, m):
    print(pow(a, b))
    print(pow(a, b, m))


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())

    if (1 <= a <= 10) and (1 <= b <= 10) and (2 <= m <= 1000):
        pow_mod_pow(a, b, m)
