import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from base_class import *
from helpers import *


class FastScan(WrapperScan):

    def handle_user_input(self):
        pass

    def extract_from_link(self, link: str):
        # extract and all urls present in the HTML code present in the link
        # use function is_same_domain to check if the urls is not on the same domain
        pass

    def is_same_domain(self, link: str):
        # check if link is same domain as website_fs (accessible as self.website_fs.root())
        # return list with all urls
        pass

    def add_link_to_tree(self, link: str):
        # create data structure to efficiently add urls without searching in tree
        # consider to rewrite use of identifiers to uniquely match paths
        # or avoid the problem checking if node already exists and then adding

        pass

    def fast_html_attack(self):
        pass

    def fast_mode(self):
        pass
