def get_meters(type_length):
    based = {'km': 1000,
             'm': 1,
             'cm': 0.01,
             'mm': 0.001}

    advanced = {'inch': 2.54 * based['cm'],
                'foot': 30.48 * based['cm'],
                'yard': 0.9144 * based['m'],
                'mile': 1609 * based['m']}

    return advanced[type_length] if type_length not in based else based[type_length]


def translate_length(parsed_str):
    length_from = get_meters(parsed_str[1])
    length_to = get_meters(parsed_str[-1])

    type_relation = length_from / length_to

    return format(type_relation * float(parsed_str[0]), "5.2e")


parsed_string = input().split(' ')

print(translate_length(parsed_string))

