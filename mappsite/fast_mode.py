import os
import sys
from bs4 import BeautifulSoup

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from base_class import *
from helpers import *
import requests
import re

links = []


class FastScan(WrapperScan):

    def handle_user_input(self):
        pass

    def extract_from_link(self, link: str, url):

        response = requests.get(url)  # json

        # making a request to a web page, in this case to website_fs
        htmlDoc = requests.get(self.website_fs.root())

        # analyze the html of the website into its parts
        soup = BeautifulSoup(htmlDoc, 'html.parser')

        # find any content with the "href" tag
        # also starting with https:// but sometimes the website may start with http!!!
        for link in soup.find_all('a',
                                  attributi={'href': re.compile("^https://")}):
            links.append(link.get('href'))
        # put everything into the list 'links'
        return links

    def is_same_domain(self, link: str):
        i = 0

        for x in range(links):
            for a in range(len(self.website_fs.root())):
                # comparing every element from links with website_fs with the length of website_fs
                # so if the website starts with https:// it will always compare the first 8 characters
                if self.website_fs.root() == links[i]:
                    link[i] = link[i][0: len(
                        self.website_fs.root())]  # the second parentheses is to compare only the website_fs length and not the rest

                    i += 1
                    return
            else:
                del links[i]
                i += 1

        # check if link is same domain as website_fs (accessible as self.website_fs.root())
        # return list with all urls
        return links

    def add_link_to_tree(self, link: str):
        # create data structure to efficiently add urls without searching in tree
        # consider to rewrite use of identifiers to uniquely match paths
        # or avoid the problem checking if node already exists and then adding

        pass

    def fast_html_attack(self):
        pass

    def fast_mode(self):
        pass
