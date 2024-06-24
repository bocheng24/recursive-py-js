const factorial = n => {

    let result = 1;

    for (let i = 1; i <= n; i++) {
        result *= i;
    }

    return result;
}

n = 5

const r = factorial(n)

console.log(r)