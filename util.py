# This file is part of graphql-expose
# See https://github.com/mateoSploit/graphql_expose for more information
# Copyright (C) Matthew Moses <mmoses.web@gmail.com>
# This program is published under a MIT license

"""
Helper functions
"""

def ask(message):
    """
    Prompts a user for input
    """
    return input("[+] {message}".format(message=message))

def log(message):
    """
    Prints a message to the console
    """
    print("[+] {message}".format(message=message))

def error(message):
    """
    Prints an error message to the console
    """
    print("[-] {message}".format(message=message))
