print("Hello world")

print(10 * (43.5 / 60) / 1.61)


def how_time(init_time='05:30', add_hours=0, add_mins=0, add_secs=0):

    def format_t(time):
        return '0' + str(time) if len(str(time)) == 1 else str(time)

    parsed_time = init_time.split(':')
    new_time_in_sec = ((add_hours + int(parsed_time[0])) * 60 + add_mins + int(parsed_time[1])) * 60 + add_secs
    new_hours = new_time_in_sec // 3600
    new_minutes = (new_time_in_sec - new_hours * 3600) // 60

    print('New time is {}:{}'.format(format_t(new_hours), format_t(new_minutes)))


how_time('06:52', add_mins=(8 * 2 + 7 * 3), add_secs=(15 * 2 + 12 * 3))



def right_justify(s):
    result = ' ' * (70 - len(s)) + str(s)
    print(result)

right_justify('alien')

def do_twice(f, value='spam'):
    f(value)
    f(value)

def print_twice(value='some'):
    print(value)
    print(value)

do_twice(print_twice)

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print ('+ - - - -'),

def print_post():
    print ('|        '),

def print_beams():
    do_twice(print_beam)
    print ('+')

def print_posts():
    do_twice(print_post)
    print ('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()