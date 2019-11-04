def sum_all(*args):
    return sum(args)


def anagrams(file):
    result = {}
    for line in file:
        word = line.strip()
        k = ''.join(sorted(word))
        if k not in result:
            result[key] = [word]
        else:
            result[key].append(word)
    return result


fin = open('words.txt')
ang = anagrams(fin)

for key, value in ang.items():
    if len(value) > 1:
        print(key, value)


