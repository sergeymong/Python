import collections

words = input().lower().strip().split(' ')

c = collections.Counter(words)

for key, count in c.items():
    print('{} {}'.format(key, count))