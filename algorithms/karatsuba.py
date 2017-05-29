def num_digits(a):
    return len(str(a))

def k_multiply(x, y, base=10):
    if num_digits(x) <= 1 or num_digits(y) <= 1:
        return x * y

    m = max(num_digits(x), num_digits(y)) / 2

    x1 = x / base**m
    x0 = x % base**m
    y1 = y / base**m
    y0 = y % base**m

    z2 = k_multiply(x1, y1)
    z0 = k_multiply(x0, y0)
    z1 = k_multiply(x1 + x0, y1 + y0) - z2 - z0

    return z2 * base**(2 * m) + z1 * base**m + z0
