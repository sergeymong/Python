def has_no_e(word):
    return word.find('e') != -1


def avoids(word, letters):
    for letter in letters:
        if letter in word:
            return True
    return False


def e_words(file):
    n_lines = 0
    not_e_word = 0
    for line in file:
        word = line.strip()
        if not has_no_e(word):
            not_e_word += 1
            print(word)
        n_lines += 1
    print('Percent of words without "e": {0:.2f}%'.format(not_e_word / n_lines * 100))


fin = open('words.txt')
e_words(fin)

print(avoids('pudg', ['a', 'e', 'm']))


