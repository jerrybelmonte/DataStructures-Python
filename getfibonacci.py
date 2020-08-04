# Simple recursive fibonacci function
def get_fib(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position - 1) + get_fib(position - 2)


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
print(get_fib(1))
print(get_fib(4))