def fib(n):

    if n == 1 or n == 2:
        print(f'Call to fib({n}), return 1')
        return 1

    print(f'Calling fibonacci({n - 1}) and fibonacci({n - 2}).')

    result = fib(n - 1) + fib(n - 2)

    print(f'Call to fibonacci({n}) returning {result}.')
    return result

if __name__ == '__main__':
    n = 10

    print(fib(n))

    # Calling fibonacci(9) and fibonacci(8).
    # Calling fibonacci(8) and fibonacci(7).
    # Calling fibonacci(7) and fibonacci(6).
    # Calling fibonacci(6) and fibonacci(5).
    # Calling fibonacci(5) and fibonacci(4).
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Call to fibonacci(6) returning 8.
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Call to fibonacci(7) returning 13.
    # Calling fibonacci(5) and fibonacci(4).
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Call to fibonacci(6) returning 8.
    # Call to fibonacci(8) returning 21.
    # Calling fibonacci(6) and fibonacci(5).
    # Calling fibonacci(5) and fibonacci(4).
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Call to fibonacci(6) returning 8.
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Call to fibonacci(7) returning 13.
    # Call to fibonacci(9) returning 34.
    # Calling fibonacci(7) and fibonacci(6).
    # Calling fibonacci(6) and fibonacci(5).
    # Calling fibonacci(5) and fibonacci(4).
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Call to fibonacci(6) returning 8.
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Call to fibonacci(7) returning 13.
    # Calling fibonacci(5) and fibonacci(4).
    # Calling fibonacci(4) and fibonacci(3).
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fibonacci(5) returning 5.
    # Calling fibonacci(3) and fibonacci(2).
    # Calling fibonacci(2) and fibonacci(1).
    # Call to fib(2), return 1
    # Call to fib(1), return 1
    # Call to fibonacci(3) returning 2.
    # Call to fib(2), return 1
    # Call to fibonacci(4) returning 3.
    # Call to fibonacci(6) returning 8.
    # Call to fibonacci(8) returning 21.
    # Call to fibonacci(10) returning 55.
