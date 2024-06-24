const powIter = (base, exp) => {
    let result = 1;

    while (exp > 0) {
        result = result * base
        exp--;
    }

    return result;
}

console.log(powIter(3, 6))
console.log(powIter(10, 3))
console.log(powIter(17, 10))

const powRecur = (base, exp) => {
    if (exp === 1) return base
    let result;

    if (exp % 2 === 0) {
        result = powRecur(base, exp / 2);
        return result * result
    }

    result = powRecur(base, (exp - 1) / 2);
    return base * result * result
}

console.log(powRecur(3, 6))
console.log(powRecur(17, 10))
console.log(powRecur(3, 500))