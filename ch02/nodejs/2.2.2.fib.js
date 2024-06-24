const fib = n => {
    if (n < 3) {
        return 1
    }

    return fib(n - 1) + fib(n - 2)
}

const n = 10

console.log(fib(n))