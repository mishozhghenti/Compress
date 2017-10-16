import sys

def prepare_character_containers(characters, characters_dictionary):
    characters.append("32")
    characters_dictionary["32"] = 0

    for i in range(144, 177):
        current_character = "225-131-" + str(i)
        characters_dictionary[current_character] = 0
        characters.append(current_character)


def prepare_couple_containers(couples, couples_dictionary):
    for i in range(len(characters)):
        for j in range(len(characters)):
            current_couple = characters[i] + " " + characters[j]
            couples.append(current_couple)
            couples_dictionary[current_couple] = 0


def character_statistics(characters, characters_dictionary, character_counter):
    result = ""
    for i in range(len(characters)):
        result = result + str('{0:.7f}'.format(float(characters_dictionary[characters[i]]) / float(character_counter)))
        if (not i == len(characters) - 1):
            result = result + " "
    result = result+"\n"
    return result


def couples_statistics(couples, couples_dictionary, couple_counter):
    result = ""
    for i in range(len(couples)):
        result = result + '{0:.7f}'.format(float(couples_dictionary[couples[i]]) / float(couple_counter))
        if (not i == len(couples) - 1):
            result = result + " "
    return result


def write_result(characters, characters_dictionary, character_counter, couples, couples_dictionary, couple_counter,
                 out_file):
    file = open(out_file, "w")
    file.write(character_statistics(characters, characters_dictionary, character_counter)+couples_statistics(couples, couples_dictionary, couple_counter))
    file.close()


from_file = sys.argv[1]
out_file = sys.argv[2]

open_file = open(from_file, 'r')
bin_file = ""
i = 0
current_symbol = ""

# a-h
characters = []  # a,b,c ....
characters_dictionary = {}  # {a:counter(a), b= counter(b)... }
prepare_character_containers(characters, characters_dictionary)

couples = []
couples_dictionary = {}
prepare_couple_containers(couples, couples_dictionary)

character_counter = 0

current_symbol = ""
couple = "32"
couple_counter = 0
for x in open_file.read():
    if (ord(x[0]) == 32):
        current_symbol = ""
        characters_dictionary["32"] = characters_dictionary["32"] + 1
        character_counter = character_counter + 1

        couple = couple + " 32"
        couples_dictionary[couple] = couples_dictionary[couple] + 1
        couple = couple[couple.index(" ") + 1:]
        couple_counter = couple_counter + 1

    else:

        if (not len(current_symbol) == 0):
            current_symbol = current_symbol + "-" + str(ord(x))
        else:
            current_symbol = current_symbol + str(ord(x))

        if (len(current_symbol) == 11):
            characters_dictionary[current_symbol] = characters_dictionary[current_symbol] + 1
            character_counter = character_counter + 1
            couple = couple + " " + current_symbol

            current_symbol = ""

            couples_dictionary[couple] = couples_dictionary[couple] + 1

            couple = couple[couple.index(" ") + 1:]
            couple_counter = couple_counter + 1

write_result(characters, characters_dictionary, character_counter, couples, couples_dictionary, couple_counter,
             out_file)
