import numpy as np
import time

def is_sorted(arr):
    return sorted(arr) == arr


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


def has_duplicates(arr):
    dates = {}
    for e in arr:
        if not dates.get(str(e)):
            dates[str(e)] = 1
        else:
            dates[str(e)] += 1
        if dates[str(e)] == 2:
            return True
    return False


def count_matches(sims):
    matched = 0
    for i in range(sims):
        matched += has_duplicates(np.random.randint(1, 365, 24))
    print('Simulation has {0:.1%} of matches.'.format(matched / sims, matched, sims))


def remove_duplicated(arr):
    elements = {}
    for e in arr:
        if elements.get(str(e)):
            continue
        else:
            elements[str(e)] = 1
    return list(elements.keys())


def remove_duplicated_f(arr):
    elements = {}
    for e in arr:
        tmp = str(e)
        if tmp in elements:
            continue
        else:
            elements[tmp] = 1
    return list(elements.keys())


def remove_duplicated_f1(arr):
    elements = {}
    for e in arr:
        tmp = str(e)
        if elements.get(tmp):
            continue
        else:
            elements[tmp] = 1
    return list(elements.keys())


def remove_duplicated_2(arr):
    return list(np.unique(arr))


def list_from_file():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def list_from_file_2():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


print(is_sorted(['b', 'a']))
print(is_anagram('rty', 'try'))

print('dict')
tt = time.time()
for _ in range(300):
    remove_duplicated(np.random.randint(1, 365, 50000))
print(time.time() - tt)

print('dict mod')
tt = time.time()
for _ in range(300):
    remove_duplicated_f(np.random.randint(1, 365, 50000))
print(time.time() - tt)

print('dict mod 2')
tt = time.time()
for _ in range(300):
    remove_duplicated_f(np.random.randint(1, 365, 50000))
print(time.time() - tt)

print('unique')
tt = time.time()
for _ in range(300):
    remove_duplicated_2(np.random.randint(1, 365, 50000))
print(time.time() - tt)

print('list_from_file')
tt = time.time()
list_from_file()
print(time.time() - tt)

print('list_from_file_2')
tt = time.time()
# ist_from_file_2()
print(time.time() - tt)
