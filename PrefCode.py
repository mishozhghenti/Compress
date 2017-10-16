import sys
import math


def read_file(file_name):
    text = ""
    file = open(file_name, 'r')
    for x in file.read():
        text += x

    all_numbers = []
    numbers = text.split(" ")
    for i in range(len(numbers)):
        all_numbers.append(int(numbers[i]))
    return all_numbers


def is_craft(all_numbers):
    sum = 0.0
    for i in range(len(all_numbers)):
        sum += (math.pow(2.0, (-1) * all_numbers[i]))
    return sum <= 1


def writeToFile(file_name, text):
    text_file = open(file_name, "w")
    text_file.write(text)
    text_file.close()


def solv(numbers, all):
    cur = 0
    all[numbers[0]] = [bin(cur)[2:].zfill(numbers[0])]

    for i in range(1, len(numbers)):
        cur += 1
        if (not numbers[i] == numbers[i - 1]):
            cur = cur * (2 ** (numbers[i] - numbers[i - 1]))

        current = bin(cur)[2:].zfill(numbers[i])
        if (numbers[i] in all):
            all[numbers[i]].append(current)
        else:
            all[numbers[i]] = [current]


from_file = sys.argv[1]
to_file = sys.argv[2]

numbers = read_file(from_file)

dictionary = {}
res = ""
if (is_craft(numbers)):
    solv(sorted(numbers), dictionary)

    for i in range(len(numbers)):
        current_key = numbers[i]

        cur_res = dictionary[current_key][0]
        res += cur_res
        if (not i == (len(numbers) - 1)):
            res += "\n"
        del dictionary[current_key][0]

writeToFile(to_file, res)
