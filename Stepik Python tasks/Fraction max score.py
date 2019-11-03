import collections

c = collections.Counter(input().split(' '))

print('{0:.2f}'.format(c['A'] / sum(c.values()), 2))
