# This file is part of graphql_expose
# See https://github.com/mateoSploit/graphql_expose for more information
# Copyright (C) Matthew Moses <mmoses.web@gmail.com>
# This program is published under a MIT license

"""
Helper functions
"""

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

def ask_multi(message):
    """
    Prompts a user and allows multi line entry
    """
    log("{message}. Use Ctrl-D when done.".format(message=message))
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    
    return "\n".join(contents)
    

def ask(message):
    """
    Prompts a user for input
    """
    return input("[+] {message} ".format(message=message))
