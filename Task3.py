import time

def decorator_1(func):       #task1 started
    def wrap(*args, **Kw):
        start = time.time()
        final = func(*args, **Kw)
        print(f"{func.__name__} call executed in {time.time() - start:.4f} sec")
        return final
    return wrap
    #ednded


@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)
    return result

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i
    return max_val