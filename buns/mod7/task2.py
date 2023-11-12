def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper

@memoize
def fibonacci(n):
    """Return the n-th Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10)) 
print(fibonacci.__name__)  
print(fibonacci.__doc__)  