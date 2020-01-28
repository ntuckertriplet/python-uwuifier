def uwuify_file(input_file):
    result = ''
    with open(input_file, 'r') as infile:
        for line in infile:
            line = line.replace('r', 'w').replace('l', 'w')
            result += line

    return result


def uwuify_string(input_string):
    result = ''
    for ch in input_string:
        if ch in "lr":
            ch = 'w'
        result += ch

    return result
