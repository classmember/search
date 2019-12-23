#!/usr/bin/env python3
'''
usage: google_suggestions.py [-h] [query [query ...]]

positional arguments:
  query       search string

optional arguments:
  -h, --help  show this help message and exit

library usage:
    >>> from google_suggestions import suggest
    >>> suggest('some')
    ['something in the water', 'some da eat', 'someone you loved', 'something in the water 2020',
     'something in the water 2020 lineup', 'something to eat', 'someone you loved lyrics',
     'something in the water 2020 tickets', 'somewhere over the rainbow', 'something in the water tickets']
'''

import requests
import json
from argparse import ArgumentParser


DEFAULT = {
    'suggestURL': 'http://suggestqueries.google.com/complete/search?client=firefox&q=',
    'headers': {'User-agent':'Mozilla/5.0'}
}

def suggest(query):
    '''Get list of top 10 Google suggestions

    Args:
        query(str): Query for Google suggestions

    Returns:
        list: a list of Google search suggestions as strings
    '''
    URL = DEFAULT['suggestURL'] + query
    response = requests.get(URL, headers=DEFAULT['headers'])
    return json.loads(response.content.decode('utf-8'))[1]

def cli_args_string(parser = ArgumentParser()):
    '''Returns space seperated string of all command line arguments

    Args:
        parser(ArgumentParser): parser for cli arguments

    Returns:
        string: all command line arguments
    '''
    parser.add_argument('query', nargs='*', help='search string')
    return ' '.join(parser.parse_args().query)

def googleSearch(query, url = 'https://www.google.com'):
    '''Returns URL as a string for the Google Search URL

    Args:
        string: search terms
        string: URL for search engine
                (default: https://www.google.com/)

    Returns:
        string: URL for search results
    '''
    with requests.session() as session:
        return requests.get(url, params={'q': query}).url

def main(args = cli_args_string()):
    if args:
        for result in suggest(args):
            print(result)

if __name__ == '__main__':
    main()
