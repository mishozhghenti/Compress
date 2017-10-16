import sys


def toBinary(n):
    res = ""
    while (n != 0):
        if (n % 2 == 1):
            res += "1"
        else:
            res += "0"
        n /= 2
    res = res[::-1]
    return res.zfill(8)


def get_codes(code_file, dictionary):
    text = ""
    file = open(code_file, 'r')
    for x in file.read():
        text += x
    tokens = text.split("\n")

    dictionary[tokens[0]] = "32"

    for i in range(144, 177):
        current_character = "225-131-" + str(i)
        dictionary[tokens[i - 144 + 1]] = current_character

def decompress(from_file, dictionary):
    open_file = open(from_file, 'r')

    bin_text = ""
    for x in open_file.read():
        bin_text += toBinary(ord(x))

    last_index = 0
    for i in range(len(bin_text)):
        if (bin_text[i] == '1'):
            last_index = i

    bin_text = bin_text[0:last_index]

    current = ""
    res_sequence = []
    for i in range(len(bin_text)):
        current += bin_text[i]
        if (current in dictionary):
            res_sequence.append(dictionary[current])
            current = ""

    file_res = ""

    for i in range(len(res_sequence)):
        if (len(res_sequence[i]) == 2):
            file_res += " "
        else:
            tokens = res_sequence[i].split("-")
            for j in range(len(tokens)):
                file_res += chr(int(tokens[j]))
    return file_res


def write_result(file_res, to_file):
    file = open(to_file, "w")
    file.write(file_res)
    file.close()


code_file = sys.argv[1]
from_file = sys.argv[2]
to_file = sys.argv[3]

dictionary = {}  # (bin_code, symbol)
get_codes(code_file, dictionary)

write_result(decompress(from_file, dictionary), to_file)
