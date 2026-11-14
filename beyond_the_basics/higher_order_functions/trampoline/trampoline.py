import types

def trampoline(f, *args, **kwargs):
    result = f(*args, **kwargs)
    while isinstance(result, types.FunctionType):
        result = result()
    return result

def factorial_rec(n, acc=1):
    if n == 0:
        return acc
    else:
        return lambda: factorial_rec(n - 1, acc * n)

def fib_rec(n, prev = 0, curr = 1):
    if n == 0:
        return curr
    else: return(lambda: fib_rec(n - 1, curr, curr + prev))


print(trampoline(fib_rec, 5))