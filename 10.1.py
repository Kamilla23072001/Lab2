def y(x):
    return x**2 + 3

print([y(x) for x in range(10, 30+1, 2)])

print(*map(y, range(10, 30+1, 2)))
