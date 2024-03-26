import os
import sys
from bs4 import BeautifulSoup 
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from base_class import *
from helpers import *
import requests
import re



class FastScan(WrapperScan):
    global links
    links = []
    

    def handle_user_input(self):
        pass

    def extract_from_link(self, link: str, url):
      
        response = requests.get(url) #json

        global urlDaAcchiappare
        urlDaAcchiappare = "www.polimi.it"
        #porcocane
  
        htmlDoc = requests.get(urlDaAcchiappare) 
  
        soup = BeautifulSoup(htmlDoc, 'html.parser') 


        # trovi tutti che hanno  con "href"  
        # quelli che iniziano con https://
        for link in soup.find_all('a',  
            attributi={'href': re.compile("^https://")}): 
            links.append(link.get('href'))
        
        return links



    def is_same_domain(self, link: str):
        i = 0
        for x in range(links):
            if urlDaAcchiappare == links[i]:
                link[i] = link[i][0: len(urlDaAcchiappare)]
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
