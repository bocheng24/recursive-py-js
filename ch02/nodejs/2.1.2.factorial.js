const factorial = n => {
    if (n === 1) return 1

    return n * factorial(n - 1);
}

const n = 5;

const r = factorial(n)
console.log(r);