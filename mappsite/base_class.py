import sys
import logging as log
import treelib as tr
import itertools


class Counter:
    def __init__(self):
        self._incs = itertools.count()
        self._decs = itertools.count()

    def inc(self):
        next(self._incs)

    def dec(self):
        next(self._decs)

    def count(self):
        return next(self._incs) - next(self._decs)


class WrapperScan:
    website_fs = None
    MAX_THRD = 10
    MAX_TIME = 2
    total_requests = Counter()
    requests_rate = 0

    def __init__(self, website: str):
        sys.setrecursionlimit(5000)
        log.basicConfig(filename='app.log', filemode='w', level=log.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - dictionary scan -- %(message)s')
        # logger = log.getLogger(__name__)
        # logger.debug('This is a debug message')

        self.website_fs = tr.Tree()
        self.website_fs.create_node(website, website)

        # check if files exists here and throw
        #         exception logger = log.getLogger(__name__)
        #         logger.exception("dictionary file not found")
        #         print(e)
        #         raise SystemExit

    def handle_user_input(self):
        # selector for mode and website with parameters
        # manage mixed modes (hybrid attacks)
        pass

    def __del__(self):
        # save file
        pass
