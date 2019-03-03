# This file is part of graphql-expose
# See https://github.com/mateoSploit/graphql-expose for more information
# Copyright (C) Matthew Moses <mmoses.web@gmail.com>
# This program is published under a MIT license

"""
Main module
"""

import sys

banner = r"""
                       _           _                                      
                      | |         | |                                     
  __ _ _ __ __ _ _ __ | |__   __ _| |______ _____  ___ __   ___  ___  ___ 
 / _` | '__/ _` | '_ \| '_ \ / _` | |______/ _ \ \/ / '_ \ / _ \/ __|/ _ \
| (_| | | | (_| | |_) | | | | (_| | |     |  __/>  <| |_) | (_) \__ \  __/
 \__, |_|  \__,_| .__/|_| |_|\__, |_|      \___/_/\_\ .__/ \___/|___/\___|
  __/ |         | |             | |                 | |                   
 |___/          |_|             |_|                 |_|                   
"""

usage = """
    commands \t|\t description
    help \t|\t displays this usage information
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

def help():
    """
    Prints usage information to the console
    """
    log(usage)

def interact(options):
    """
    Controls interactive prompt with user
    """
    log("Interacting with: {url}".format(url=options["url"]))
    log("Type your command or \"help\" for usage.")
    exit = False
    while not exit:
        command = ask("$ ")
        if command in [ "exit", "quit" ]:
            log("Exiting...")
            exit = True
        elif "help" in command:
            help()
        else:
            error("Unrecognized command: {command}".format(command=command))
            help()
        

def setup():
    """
    Gets required details from user so we can
    start interacting with a GraphQL API
    """
    url = ask("URL: ")
    return { "url": url }   

if __name__ == "__main__":
    """
    Main routine
    """
    try:
        print(banner)
        options = setup()
        interact(options)
    except KeyboardInterrupt:
        pass
