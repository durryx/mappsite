from helpers import *
import sys
import logging as log


class WrapperScan:
    website_fs = None
    MAX_THRD = 10

    def __init__(self, website: str):
        sys.setrecursionlimit(5000)
        log.basicConfig(filename='app.log', filemode='w', level=log.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - dictionary scan -- %(message)s')
        # logger = log.getLogger(__name__)
        # logger.debug('This is a debug message')

        self.website_fs = tr.Tree()
        self.website_fs.create_node(website, website)

    def extract_from_link(self):
        pass

    def is_same_domain(self):
        pass

    def fast_scan(self):
        pass

    def __del__(self):
        # save file
        pass
