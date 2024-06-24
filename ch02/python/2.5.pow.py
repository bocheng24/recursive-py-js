def pow_iter(base, exp):

    result = 1

    for _ in range(exp):
        result *= base

    return result

print(pow_iter(3, 6))
print(3 ** 6)

def pow_recur(base, exp):

    if exp == 1:
        return base

    if exp % 2 == 0:
        result = pow_recur(base, exp / 2)
        return result * result

    result = pow_recur(base, (exp - 1) / 2)
    return base * result * result

print(pow_recur(3, 6))
print(pow_recur(17, 6))