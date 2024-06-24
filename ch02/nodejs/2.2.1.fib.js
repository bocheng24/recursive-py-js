const fib = n => {
    let a = 1;
    let b = 1;

    for (let i = 1; i < n; i++) {
        let nextNumber = a + b;
        a = b;
        b = nextNumber;
    }

    return a;
}

const n = 10;
console.log(fib(n));
