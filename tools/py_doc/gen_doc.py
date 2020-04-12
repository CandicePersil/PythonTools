#!/usr/bin/python3.8
# -*-coding:Utf-8 -*


"""gen_doc.py: generate python and markdown docs for python modules"""
"""
   Functions: import modules, write to file in work directory, 
   write python doc and write markdown doc, get module name
"""
"""Input: string module path"""


__author__ = "Candice P"
__copyright__ = "Copyright 2020, Python tools"
__version__ = "1.0.0"


import inspect
import os
import argparse
from importlib import import_module


def import_mod(modulename):
    """Import module from name

    :param modulename: name of the module to import
    :type modulename:  str
    :return:           a module
    :rtype:            class module
    """
    return import_module(modulename)


def write_to_file(filename, content):
    """Write content to file into working directory

    :param filename: name of file containing extension
    :type filename:  str
    :param content:  text
    :type content:   str
    :return:         file path
    :rtype:          str
    """
    path = "./"+filename
    with open(path, "w") as modf:
        modf.write(content)
    return path


def write_markdownform(module):
    """Write markdown documentation from python doc contained into a module

    :param module: python module
    :type module:  class module
    :return:       markdown documentation
    :rtype:        str
    """
    functionlist = []
    for obj in inspect.getmembers(module):
        if inspect.isfunction(obj[1]):
            functionlist.append(obj)

    tmpmoduledoc = ''
    moduledoc = "# "+inspect.getdoc(module)
    print("=" * len(moduledoc))
    print(moduledoc)
    tmpmoduledoc += moduledoc + "\n"
    print("=" * len(moduledoc) + "\n")
    tmpmoduledoc += "\n\n"

    for list in functionlist:
        for data in list:
            if not callable(data):
                print("### function : " + data)
                tmpmoduledoc += "function : " + data + "\n"
                print("=" * len("function : " + data))
                tmpmoduledoc += "-"*6 + "\n"
            else:
                print(inspect.getdoc(data))
                tmpmoduledoc += "```\n"+inspect.getdoc(data) + "\n```"
        print("\n")
        tmpmoduledoc += "\n"

    return tmpmoduledoc


def get_modulename(path):
    """Get the name of a module from the module path

    :param path: path of the module file
    :type path:  str
    :return:     module name without file extension
    :rtype:      str
    """
    filenameext = os.path.basename(path)
    filename = os.path.splitext(filenameext)[0]
    return filename


def gen_pymddoc(modulepath):
    """Call write methods from module path in order to generate module documentation

    :param modulepath: module path
    :type modulepath:  str
    :return:           python md documentation path
    :rtype:            str
    """
    modulename = get_modulename(modulepath)
    import_mod(modulename)
    content = write_markdownform(import_mod(modulename))
    mddocpath = write_to_file(modulename+".md", content)

    return mddocpath


def main():
    """main function - execute only if run as a script

    description: degenerate python and markdown doc into local working directory file

    """
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("modulepath", type=str, help="Module path")

    args = parser.parse_args()

    if args.modulepath is not None:
        if os.path.exists(args.modulepath):
            moduledocpath = gen_pymddoc(args.modulepath)
            print("Python documentation generated: {}".format(moduledocpath))
        else:
            print("Module file doesn't exist")
            exit(1)
    else:
        print('An input is needed!')
        exit(1)


if __name__ == "__main__":
    main()
