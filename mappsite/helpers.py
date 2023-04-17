import requests as rq
import copy
import treelib as tr
import concurrent.futures as th


def test_connection(website: str, dir_string: str):
    # check if dir_string is a valid link for website
    # website form = "http://www.urltest.domain"
    # dir_string form = "directory_name"

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
        return False, None

    # check redirections' status if they exist and save them -- error for invalid redirections
    # see https://requests.readthedocs.io/en/latest/user/quickstart/#redirection-and-history
    if len(response.history) == 1:
        return True, None

    # explore redirections
    # |url 1| --> |url 2| --> |url 3| --> status code >= 400 STOP
    temp_tree = tr.Tree()
    temp_tree.create_node(full_url, full_url)
    chain = copy.deepcopy(full_url)
    for resp in response.history[1:]:
        if resp.status_code >= 400:
            break
        temp_tree.create_node(resp.url, resp.url, parent=chain)
        chain = resp.url

    return True, temp_tree


def recursive_cat(website_fs: tr.Tree, node: tr.Node, link: str):
    if node.is_root():
        return link
    else:
        prev_node_id = node.predecessor(website_fs.identifier)
        prev_node = website_fs.get_node(prev_node_id)
        link = prev_node.tag + '/' + link
        return recursive_cat(website_fs, prev_node, link)


def link_cat(website_fs: tr.Tree, node: tr.Node):
    return recursive_cat(website_fs, node, '') + node.tag


def handle_user_input(thread_pool: [th.Future]):
    on_flag = True
    one_thread_check = lambda proc: True if (proc.done() == True) else False

    while on_flag:
        # user input and output - use ncurses?
        if all(map(one_thread_check, thread_pool)):
            on_flag = False



def tree_append(website_fs: tr.Tree, sub_dir, dir_string):
    # append dir_string as a valid resource to sub_dir in website_fs
    # or append small tree to node
    return
