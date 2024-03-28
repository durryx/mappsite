from argparse import ArgumentParser
import pathlib
from base_class import WrapperScan


def is_valid_file(parser, file):
    # check if file is the path is valid and if the file is creatable
    # see https://stackoverflow.com/questions/39349653/arg-parse-parse-file-name-as-string-python
    # see https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
    pass


def is_valid_bitrate(parser, rate):
    # check if string is form of "300Kbit/s" or others
    pass


if __name__ == '__main__':
    parser = ArgumentParser(
        prog="mappsite",
        description="",
        allow_abbrev=False
    )
    parser.add_argument('--version', '-v', action="store_false", help="display mappsite use")
    parser.add_argument("--mode", "-m", choices=("auto", "url", "html", "dict"), nargs='?',
                        default="auto", help="manually specify init mode (can be switched at runtime)")
    parser.add_argument("url", type=str)
    parser.add_argument('-s', '--save', type=lambda file: is_valid_file(parser, file),
                        metavar="tree.xml", help="save website tree to file")
    parser.add_argument('-i', '--image', type=lambda file: is_valid_file(parser, file),
                        metavar="image.png", help="create a image view of the website tree")
    # parser.add_argument('-l', '--limit', type=lambda rate: is_valid_bitrate(parser, rate),
    #                    metavar="200Kbit/s")


