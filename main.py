import json
import random
import time

from Task1 import kwargsAceeptFun
Kw= kwargsAceeptFun(name="Mumtozmhal", age=19)  # etc inputs #1

from Task2 import typeBasedTransformer
final = typeBasedTransformer(  # 2
        key=input()
    )
for key, val in final.items():
        print(f"{val}")

from Task3 import decorator_1
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
if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
