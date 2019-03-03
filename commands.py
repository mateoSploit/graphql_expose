# This file is part of graphql-expose
# See https://github.com/mateoSploit/graphql-expose for more information
# Copyright (C) Matthew Moses <mmoses.web@gmail.com>
# This program is published under a MIT license

"""
Support code from program commands
"""

from util import log

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
