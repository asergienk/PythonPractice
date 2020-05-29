def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1 
    i = 2 
    list = [0, 1]
    while i <= n-1:
        list.append(list[i-2] + list[i-1])
        i += 1
    return list[n-1]


print(fib(7))
