# This file is part of graphql_expose
# See https://github.com/mateoSploit/graphql_expose for more information
# Copyright (C) Matthew Moses <mmoses.web@gmail.com>
# This program is published under a MIT license

"""
Main module
"""

import logging
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
""" # Thanks to http://patorjk.com/software/taag/

from commands import run_query
from commands import help
from exs import ApplicationCriticalError
from util import log
from util import error
from util import ask

DEFAULT_URL = "http://localhost:4000/graphql"

def interact(options):
    """
    Controls interactive prompt with user
    """
    url = options["url"]
    log("Interacting with: {url}".format(url=url))
    log("Type your command or \"help\" for usage.")
    exit = False
    while not exit:
        command = ask("$")
        if command in [ "exit", "quit" ]:
            log("Exiting...")
            exit = True
        elif "help" == command:
            help()
        elif "query" == command:
            result = run_query(url)
            if result:
                log("Response: {result}".format(result=result))
        else:
            error("Unrecognized command: {command}".format(command=command))
            help()
        

def setup():
    """
    Gets required details from user so we can
    start interacting with a GraphQL API
    """
    url = ask("URL [{default_url}]: ".format(default_url=DEFAULT_URL)).strip()
    if not url:
        url = DEFAULT_URL
    else:
        log("User provided \"{url}\"".format(url=url))
    
    # TODO Also, validate that the URL is valid
    if not url:
        raise ApplicationCriticalError("Invalid URl detected.")

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
    except ApplicationCriticalError as ex:
        error("Critical error detected. Application must exit... Error: {msg}".format(msg=ex))
    except Exception:
        logging.exception("Unhandled exception")
