from helpers import *


# to reimplement iteratively TO-FIX
def gen_list(paths_list, length, string):
    # if length == 0:
        # for char in char_dictionary:
            # append to paths_list string + char
    # else:
        # for char in char_dictionary:
            # gen_list(paths_list, length-1, string + char)
    pass


def bruteforce_attack(parent, tree_structure, paths_list, depth):
    # given the cardinality of char_dictionary C
    # list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    # if depth == path_limit:
        # return

    # inc = C ** (path_limit - depth)
    # for i in range C ** depth
        # index = i*inc - 1
        # path = paths_list[index][:depth]
        # test_connection(parent, path, tree_structure)

    bruteforce_attack(parent, tree_structure, paths_list, depth + 1)


def bruteforce_mode(website, tree_structure):
    # initialize url_list with / website
    # initialize paths_list -- gen_list

    # while True
        # for url in url_list
            # launch thread bruteforce_attack(url, tree_structure, paths_list, 0)
        # handle_user_input()
        # threads joined
        # url_list = last elements of maximum depth in tree
    pass

