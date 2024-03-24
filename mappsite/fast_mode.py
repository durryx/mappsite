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
        # return list with all urls
        pass

    def is_same_domain(self, link: str):
        # check if link is same domain as website_fs (accessible as self.website_fs.root())
        pass

    def add_link_to_tree(self, link: str):
        # given link check if it is already present in the tree
        # if it is not then break it down to all minor paths and add them
        # ex. www.polimi.it/chi-siamo/path/another/page.html
        # 1 "chi-siamo/" present -> no action
        # 2 "path/" present -> no action
        # 3 "another/" not present -> add to tree
        # 4 "page.html/" not present -> add to tree
        pass

    def fast_html_attack(self):
        pass

    def fast_mode(self):
        pass
