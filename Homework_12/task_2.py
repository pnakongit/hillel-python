def new_format(string):
    format_string = ''
    counter = 1
    for i in string[::-1]:
        if counter > 3:
            format_string += '.' + i
            counter = 2
        else:
            format_string += i
            counter += 1
    return format_string[::-1]


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
print('success')


def new_format(string):
    symbols = [y + '.' if i % 3 == 0 and i != 0 else y for i, y in enumerate(string[::-1])]
    return ''.join(symbols[::-1])


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
print('success')
