import sys
import Queue


class Node:
    prob = 0.0
    one = None
    zero = None


def read_file(file_name):
    text = ""
    file = open(file_name, 'r')
    for x in file.read():
        text += x

    all_numbers = []
    count = text.split("\n")
    num_count = int(count[0])
    numbers = count[1].split(" ")

    for i in range(num_count):
        all_numbers.append(float(numbers[i]))
    return all_numbers


from_file = sys.argv[1]
out_file = sys.argv[2]
probabilities = read_file(from_file)


def get_codes_rec(root, code, dictionary):
    if (root.zero is None and root.one is None):
        if (not root.prob in dictionary):
            dictionary[root.prob] = [code]
        else:
            dictionary[root.prob].append(code)
        return
    get_codes_rec(root.zero, code + "0", dictionary)
    get_codes_rec(root.one, code + "1", dictionary)


def get_codes(root, dictionary):
    get_codes_rec(root, "", dictionary)


def write_result(file_name, text):
    file = open(out_file, "w")
    file.write(text)
    file.close()


def solve(probabilities, out_file):
    queue = Queue.PriorityQueue()

    for i in range(len(probabilities)):
        node = Node()
        node.prob = probabilities[i]
        queue.put((probabilities[i], node))

    root = None
    while not queue.empty():
        zero_p, zero_node = queue.get()
        if (queue.empty()):
            break
        one_p, one_node = queue.get()

        curr_node = Node()
        curr_node.prob = zero_p + one_p
        curr_node.zero = zero_node
        curr_node.one = one_node

        queue.put((curr_node.prob, curr_node))
        root = curr_node
    dictionary = {}
    get_codes(root, dictionary)

    res = ""
    sum = 0.0

    for i in range(len(probabilities)):
        sum +=float( len(dictionary[probabilities[i]][0]) * float(probabilities[i]))
        res += dictionary[probabilities[i]][0]
        del dictionary[probabilities[i]][0]

        if (not i == len(probabilities) - 1):
            res += "\n"
    write_result(out_file, res)


solve(probabilities, out_file)
