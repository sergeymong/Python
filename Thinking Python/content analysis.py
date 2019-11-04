import re
import time


def read_to_list(filename):
    file = open(filename)
    words = []
    for line in file:
        some_words = line.strip().split(' ')
        for word in some_words:
            tmp = re.sub(r'[^\w]+', '', word.lower())
            if tmp != '':
                words.append(tmp)
    return words


def uniq_words(words_list):
    words = len(set(words_list))
    return words


def calc_words(words_list):
    words = {}
    for word in words_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def print_top_20(words_list):
    words = calc_words(words_list)
    words = sorted(words.items(), key=lambda kv: kv[1], reverse=True)
    counter = 0
    print('Top 20 words:')
    for key, value in words[0:20]:
        counter += 1
        print('{}: {} {}'.format(counter, key, value))


d = read_to_list('60611-0.txt')
print('Overall words in book: {}, unique words: {}'.format(len(d), uniq_words(d)))
print_top_20(d)

