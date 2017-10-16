import sys


def get_codes(code_file, dictionary):
    text = ""
    file = open(code_file, 'r')
    for x in file.read():
        text += x
    tokens = text.split("\n")

    dictionary["32"] = tokens[0]

    for i in range(144, 177):
        current_character = "225-131-" + str(i)
        dictionary[current_character] = tokens[i - 144 + 1]


def read_file(from_file, text):
    open_file = open(from_file, 'r')
    current_symbol = ""

    for x in open_file.read():
        if (ord(x[0]) == 32):
            current_symbol = ""
            text.append("32")
        else:
            if (not len(current_symbol) == 0):
                current_symbol = current_symbol + "-" + str(ord(x))
            else:
                current_symbol = current_symbol + str(ord(x))

            if (len(current_symbol) == 11):
                text.append(current_symbol)
                current_symbol = ""


def write_result(res, to_file):
    file = open(to_file, "w")
    file.write(res)
    file.close()


def binToDecimal(binary):
    dec_res = 0
    for i in xrange(0, len(binary)):
        power = 2 ** (7 - i)
        k = 1
        if (binary[i] == "0"):
            k = 0
        dec_res += power * k
    return dec_res


def compress(text_sequence, code_dictionary):
    res = ""
    for i in range(len(text_sequence)):
        res += code_dictionary[text_sequence[i]]

    res += "1"
    rem_bits = len(res) % 8
    sufix = ""
    if (not rem_bits == 0):
        sufix.zfill(8 - rem_bits)
    res += sufix

    recovered_text = ""
    for x in xrange(0, len(res), 8):
        recovered_text += chr(binToDecimal(res[x:x + 8]))
    return recovered_text


code_file = sys.argv[1]
from_file = sys.argv[2]
to_file = sys.argv[3]

code_dictionary = {}  # a- 010101....
get_codes(code_file, code_dictionary)

text_sequence = []  # "current text ...."
read_file(from_file, text_sequence)

write_result(compress(text_sequence,code_dictionary), to_file)
