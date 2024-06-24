def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


if __name__ == '__main__':
    n = 5
    r = factorial(5)

    print(r)