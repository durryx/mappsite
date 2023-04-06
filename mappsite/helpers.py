import requests as rq
import copy
import treelib as tr


# return a boolean and a optional redirection tree
def test_connection(website: str, dir_string: str):
    # check if dir_string is a valid link for website
    # website form = "htttp://www.urltest.domain"
    # dir_string form = "directory_name" 

    # makes the srings raw
    website = r"{}".format(website)
    dir_string = r"{}".format(dir_string)
    full_url = f"{website}/{dir_string}"

    # testing full url
    response = rq.head(full_url, allow_redirects=True)

    # 1xx - informational
    # 2xx - success
    # 3xx - redirection
    # 4xx - client error and so on with errors
    if response.status_code >= 400:
        return False

    # check redirections' status if they exist and save them -- error for invalid redirections
    # see https://requests.readthedocs.io/en/latest/user/quickstart/#redirection-and-history
    if not response.history:
        return True

    # explore redirections
    # |url 1| --> |url 2| --> |url 3| --> status code >= 400 STOP
    temp_tree = tr.Tree()
    temp_tree.create_node(full_url, full_url)
    chain = copy.deepcopy(full_url)
    for resp in response.history:
        if resp.status_code >= 400:
            break
        temp_tree.create_node(resp.url, resp.url, parent=chain)
        chain = resp.url

    return [True, temp_tree]


def tree_append(tree_structure, sub_dir, dir_string):
    # append dir_string as a valid resource to sub_dir in tree_structure
    # or append small tree to node
    return


def load_batch(file, index, stride):
    # tries to open the file
    try:
        with open(file, "r") as f:
            # reads lines between index and index+stride
            for _ in range(index):
                next(file)
            batch = [next(file) for _ in range(stride)]
        return batch
    except FileNotFoundError:
        print("\nCan't find the file")
        return False
    finally:
        print("\nFile does not exist")
        return False

# return full link string given node
def link_cat(tree_structure: tr.Tree, node: tr.Node, link: str):
    if node.is_root():
        return link
    else:
        prev_node_id = node.predecessor(tree_structure.identifier)
        prev_node =  tree_structure.get_node(prev_node_id)
        link = prev_node.tag + '/' + link
        return link_cat(tree_structure, prev_node, link)


def dictionary_attack(tree_structure: tr.Tree, parent: tr.Node, file: str):
    # inizialize stride to a default value of 2000
    stride: int = 2000
    index, success = 0, 0
    # inizialize var with first batch of a file - load_batch
    batch: list = load_batch(file, index, stride)
    # check if batch is loaded correctly
    if batch:
        print("\nBatch laoded correctly")
    else:
        print("\nAn error occured while loading the new batch")
        return False

    partial_link = link_cat(tree_structure, parent, "")

    while True:
        for index, word in enumerate(batch):
            # parent.data takes the used payload associated by the user to the node id
            # word[:-1] is necessary because it has a "\n" on the end
            outcome, red_tree = test_connection(partial_link, word[:-1], tree_structure)

            if red_tree is not None:
                # tree_append
            elif outcome:
                print(f"\nNew dir found: {parent.data}/{word}")
                success += 1
                # tree_append()


        batch = load_batch(file, index+stride, stride)
        if batch:
            print("\nBatch laoded correctly")
        else:
            return False

    return True


def handle_user_input():
    # while True:
    # print and get relevant info
    # check if thread has joined
    pass


def automatic_mode(website, file, tree_structure):
    # initialize list with / website

    # while True
        # for link in list
            # launch thread with dictionary_attack with link
            # handle_user_input()
            # threads joined
        # list = select elements with max depth from tree
    pass


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
    # given max paths length path_limit

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
