import time


def sum_array(arr):
    arr = arr.copy()
    if len(arr) < 2:
        if len(arr) == 0:
            return 0
        else:
            return arr[0]
    else:
        return arr.pop() + sum_array(arr)


def sum_array_2(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])


def count_array(arr):
    if not arr:
        return 0
    else:
        return count_array(arr[1:]) + 1


def max_element(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        sub_max = max_element(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max


def qsort(arr):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            return arr[::-1]
    else:
        base = arr[0]
        less = []
        # less = [i for i in arr[1:] if i < base]
        more = []
        for e in arr[1:]:
            if e < base:
                less += [e]
            else:
                more += [e]
        return qsort(less) + [base] + qsort(more)


start_time = time.time()

array = [0, 3, 5, 15, 45, 12, 1, 115, 2, 1111, 5, 5, 165]

print(qsort(array))
print("--- %s seconds ---" % (time.time() - start_time))
