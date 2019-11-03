def encrypt(lag, message):
    dictionary = ' abcdefghijklmnopqrstuvwxyz'
    dict_len = len(dictionary)
    res = ''

    for m in message:
        elem = dictionary.find(m)
        tot_lag = (elem + lag) % dict_len
        res += dictionary[tot_lag]

    return res


length = int(input().strip())
mes = input().strip()

print('Result: "{}"'.format(encrypt(length, mes)))
