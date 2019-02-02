import numpy as np


w = np.array([0, 0, 0])

examples = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]])  # везде нулевой элемент = 1, потому что он фиктивный
                                                                  # и такой всегда

def Target(ex):
    if ex[1] == 1 and ex[2] == 0.3:
        return 1
    elif ex[1] == 0.4 and ex[2] == 0.5:
        return 1
    elif ex[1] == 0.7 and ex[2] == 0.8:
        return 0


def predict(example):
    sum = example[0]*w[0] + example[1]*w[1] + example[2]*w[2]
    print('example:', example)
    print('sum:', sum)
    if sum > 0:
        return 1
    else:
        return 0


perfect = False
while not perfect:
    perfect = True
    for e in examples:
        print('e:', e)
        if predict(e) != Target(e):
            perfect = False
            if predict(e) == 0:
                w = w + e
                print("w:", w)
            else:
                w = w - e
                print("w:", w)
print("final answer:", w)

