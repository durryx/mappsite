import requests as rq

def test_connection(website, dir_string):
    # check if dir_string is a valid link for website
    # website form = "htttp://www.urltest.domain"
    # dir_string form = "directory_name" 
    
    # makes the srings raw
    website = r"{}".format(website)
    dir_string = r"{}".format(dir_string)

    # full url that will be tested
    full_url = f"{website}/{dir_string}"

    # testing full url
    response = rq.get(full_url)
    print(f"Testing {full_url}")
    if response.status_code == 200:
        return True
    
    return False

def tree_append(tree_structure, sub_dir, dir_string):
    # append dir_string as a valid resource to sub_dir in tree_structure
    return
def link_bruteforce(website, sub_dir_, tree_structure):
    # loop over possible subdirectories trying with all possible char combinations
    return

