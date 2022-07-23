def fibonacci(n):
    fib = [0] * (n+1)
    for i in range(len(fib)):
        if i == 0:
            fib[i] = (1, 0)
        elif i == 1:
            fib[i] = (0, 1)
        else:
            fib[i] = tuple([sum(tup) for tup in zip(fib[i-1], fib[i-2])])
    return fib[n]

T = int(input())

for _ in range(T):
    N = int(input())
    result = fibonacci(N)
    print(result[0], result[1])