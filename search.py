#!/usr/bin/env python3

from argparse import ArgumentParser
try:
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found") 


def cli_args_string(parser = ArgumentParser()):
    '''Returns space seperated string of all command line arguments

    Args:
        parser(ArgumentParser): parser for cli arguments

    Returns:
        string: all command line arguments
    '''
    parser.add_argument('query', nargs='*', help='search string')
    return ' '.join(parser.parse_args().query)

def main():
    query = cli_args_string()
    for link in search(query, tld="com", num=10, stop=10, pause=1): 
        print(link) 

if __name__ == '__main__':
    main()
