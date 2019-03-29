# This file is part of graphql_expose
# See https://github.com/mateoSploit/graphql_expose for more information
# Copyright (C) Matthew Moses <mmoses.web@gmail.com>
# This program is published under a MIT license

"""
Support code from program commands
"""

import json
import requests
from util import ask
from util import ask_multi
from util import log
from util import error
import urllib3

usage = """
    commands \t|\t description
    help \t|\t displays this usage information
    introspect \t|\t performs introspection on API for query type objects
    quit|exit \t|\t exits application
"""

def help():
    """
    Prints usage information to the console
    """
    log(usage)

def run_query(url):
    query = ask_multi("What's the query?")
    log("Executing query: {query}".format(query=query))
    result = gql_call(url, query)
    if result:
        log("Response: {result}".format(result=result))

def gql_call(url, query):
    try:
        request = requests.post(url, json={ "query": query })
    except requests.exceptions.RequestException as ex:
        error("Unable to connect to url")
    else :
        if request.status_code == 200:
            try:
                return request.json()
            except ValueError:
                error("Could not parse return payload into valid JSON")
        else:
            error("Query failed. {error}".format(error=request.text))

def query_type_introspect(url, name):
    """
    Performs introspection on a specific query type
    """
    log("Introspecting \"{name}\" query type...".format(name=name))
    get_query_type_details_query = """
    {
        __type(name: \"%s\") {
            name
            kind
            fields {
                name
                type {
                    name
                    kind
                }
            }
        }
    }
    """ % (name)
    result = gql_call(url, get_query_type_details_query)
    log(json.dumps(result, indent=4))


def introspect(url):
    """
    Performs introspection on a GraphQL API
    """
    list_query_type_query = """
    {
        __schema {
            types {
                name
            }
        }
    }
    """
    query_types = []
    result = gql_call(url, list_query_type_query)
    if result is None:
        return
        
    for entry in result["data"]["__schema"]["types"]:
        if entry["name"] and (entry["name"].startswith("__") or entry["name"] in ["String", "Boolean"]):
            continue
        else:
            query_types.append(entry["name"])

    log("Available query types: ")
    counter = 0
    for query_type in query_types:
        log("\t[{id}] {name}".format(id=counter, name=query_type))
        counter += 1
    exit = False
    while not exit:
        answer = ask("Enter number for details (also, \"a\" to dump all or \"r\" to return): ")
        if answer.isdigit():
            index = int(answer.strip())
            try:
                name = query_types[index]
            except IndexError:
                error("Not a valid selection: {index}".format(index=index))
            else:
                log("More info on {id}".format(id=name))
                query_type_introspect(url, name)
        elif answer == "r":
            exit = True
        elif answer == "a":
            exit = True
            for query_type in query_types:
                query_type_introspect(url, query_type)
        else:
            error("Unrecognized input: {answer}".format(answer=answer))
