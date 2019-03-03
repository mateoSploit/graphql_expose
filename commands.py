# This file is part of graphql_expose
# See https://github.com/mateoSploit/graphql_expose for more information
# Copyright (C) Matthew Moses <mmoses.web@gmail.com>
# This program is published under a MIT license

"""
Support code from program commands
"""

import requests
from util import ask
from util import ask_multi
from util import log
from util import error

usage = """
    commands \t|\t description
    help \t|\t displays this usage information
    quit|exit \t|\t exits application
"""

def help():
    """
    Prints usage information to the console
    """
    log(usage)

def run_query(url):
    return gql_call(url)

def gql_call(url):
    query = ask_multi("What's the query?")
    log("Executing query: {query}".format(query=query))
    request = requests.post(url, json={ "query": query })
    if request.status_code == 200:
        return request.json()
    else:
        error("Query failed. {error}".format(error=request.text))
    
