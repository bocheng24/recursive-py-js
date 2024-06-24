def fib(n):

    a, b = 1, 1

    for i in range(1, n):
        a, b = b, a + b
        print(f'i: {i} -- a: {a}, b: {b}')

    return a

if __name__ == '__main__':
    n = 10
    print(fib(n))