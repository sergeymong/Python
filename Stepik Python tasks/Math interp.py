# plus, minus, multiply, divide

import operator


d = {
        'plus': operator.add,
        'minus': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv
    }


inp = input().strip().split(' ')

res = d[inp[1]](int(inp[0]), int(inp[2]))

print(res)


