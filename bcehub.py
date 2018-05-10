import sys

'''
Braces tell the Bash shell to generate what's called the "Cartesian product" of
the given set, where elements of the set are comma-separated. The problem at
hand is to implement this feature of Bash, i.e. produce the same output as Bash
does for a given input string.

For example:
$ echo a{b,c}d{e,f,g}hi
abdehi abdfhi abdghi acdehi acdfhi acdghi
$ echo a{b,c{d,e,f}g,h}ij{k,l}
abijk abijl acdgijk acdgijl acegijk acegijl acfgijk acfgijl ahijk ahijl

In your response, please send (or link to github, etc):
(1) Your solution, written in Java or Python
(2) Instructions on how to run the code
(3) Any unit tests that you wrote to demonstrate the correctness of your solution
'''


def bash_cartesianprod(string):                                # main
    '''if isinstance(string, str) == False:                    # check if valid string, may not need
        print("Not a valid string")
    '''
    if ' ' in string:                                          # remove white space from passed string
        string = string.strip()

    if string.count('{') != string.count('}'):                 # check number of sets
        raise InvalidString

    else:

        outside_char, inside_char = extract_char(string)       # helper function returns lists of characters within string
        return cartesian_product(outside_char, inside_char)


def split_passed_str(string):                                  # function breaks up string into characters, no commas or brackets

    if ' ' in string:
        string = string.strip()

    substr_list = []
    left_char_index = 0
    counter = 0

    for i, char in enumerate(string):
        if char == '{':
            counter += 1                                    # start counting opening brackets
        elif char == '}' and counter > 0:
            counter -= 1                                    # cancel out/subtract with closing brackets
        elif char == ',' and counter == 0:                  # brackets cancelled out, encounter commas
            substr_list.append(string[left_char_index:i])   # add char before comma to list
            left_char_index = i + 1                         # adjust index of list

    substr_list.append(string[left_char_index:len(string)])       # continue adding to list if not previous cases

    return substr_list


def extract_char(string):                                   # pull out characters, push into list depending on location within string

    if ' ' in string:
        string = string.strip()

    outside_char = []
    inside_char = []

    left_char_index = 0
    counter = 0
    for i, char in enumerate(string):
        if char == '{':
            if counter == 0:
                outside_char.append(string[left_char_index:i])     # push outside characters into list
                left_char_index = i + 1
            counter += 1
        elif char == '}' and counter > 0:
            counter -= 1
            if counter == 0:
                inside_char.append(split_passed_str(string[left_char_index:i])) # push inside characters into list
                left_char_index = i + 1

    outside_char.append(string[left_char_index:len(string)])

    return (outside_char, inside_char)


def cartesian_product(outside_char, inside_char):                  # cartesian_product function returns list of products
    cartesian_prod_list = []
    if len(inside_char) == 0:
        return outside_char
    else:
        characters = cartesian_product(outside_char[1:], inside_char[1:])
        for i in inside_char[0]:
            for j in bash_cartesianprod(i):
                for k in characters:
                    cartesian_prod_list.append(outside_char[0] + j + k)
    return cartesian_prod_list

class InvalidString(Exception):
    pass

if __name__ == "__main__":
    try:
        print (' '.join(bash_cartesianprod(sys.argv[1])))
    except InvalidString:
        print ("Invalid sets, can not return Cartesian product")
    except IndexError:
        print ("Enter valid string to get Cartesian product")
