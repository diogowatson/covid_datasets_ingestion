import argparse


def create_argument_parser():
    """
    argument parser
    basic usage:
        parser = create_argument_parser()
        args = parser.parse.parse_args()
    """
    arg_parser = argparse.ArgumentParser(description='Script to parser arguments')
    arg_parser.add_argument('--cloud',
                            type=str,
                            help='define cloud service',
                            required=False)
    arg_parser.add_argument('--bucket',
                            type=str,
                            help='path to gcp bucket',
                            required=False)
    return arg_parser
