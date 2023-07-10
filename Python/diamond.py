def rows(letter):
    base = ord('A')
    index = ord(letter) - base

    line_template = [' ' for i in range(0, index + 1)]
    result = []

    for i in range(0, index + 1):
        s = line_template[:]
        s[-(i + 1)] = chr(i + base)

        reversed_s = s[:]
        reversed_s.reverse()
        s = s + reversed_s[1:]

        s_string = list(map(str, s))
        line = ''.join(s_string)
        result.append(line)

    reversed_result = result[:]

    for i in range(len(reversed_result) - 2, -1, -1):
        result.append(reversed_result[i])

    # return convert_list_to_string(result)
    return result


def convert_list_to_string(list_of_strings):
    result = ""
    for s in list_of_strings:
        result += s
        result += '\n'
    return result


print(rows('A'))
print(rows('B'))
print(rows('C'))
print(rows('D'))
print(rows('E'))
print(rows('Z'))
