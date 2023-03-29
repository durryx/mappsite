import requests as rq
import copy


def test_connection(website, dir_string, tree_structure):
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
    if not response.status_code < 400:
        return False

    # check redirections' status if they exist and save them -- error for invalid redirections
    # see https://requests.readthedocs.io/en/latest/user/quickstart/#redirection-and-history
    if not response.history:
        return True

    # explore redirections
    # |url 1| --> |url 2| --> |url 3| --> status code >= 400 STOP
    chain = copy.deepcopy(full_url)
    for resp in response.history:
        if resp.status_code >= 400:
            break
        tree_append(tree_structure, chain, resp.url)
        chain = resp.url

    return True


def tree_append(tree_structure, sub_dir, dir_string):
    # append dir_string as a valid resource to sub_dir in tree_structure
    return


def link_bruteforce(website, sub_dir_, tree_structure, chars_num):
    # loop over possible subdirectories trying with all possible char combinations

    return
