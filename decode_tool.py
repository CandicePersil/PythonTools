#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

"""decode_tool.py: Encode and decode strings"""
"""Functions: base64, gzip, url encode and decode, base 64 decode and inflate"""
"""Input: strings, file"""

import argparse
import urllib.parse as urlparse
import zlib
import base64

__author__ = "Candice P"
__copyright__ = "Copyright 2020, Python tools"
__version__ = "1.0.0"


def url_encode(url):
    """
    :function url_encode: encode string
    :param url:           url or query string
    :return:              encoded url/query string
    """
    return urlparse.quote(url)


def url_decode(url):
    """
    :function url_decode: decode url encoded string
    :param url:           url or query string
    :return:              decoded url/query encoded string
    """
    return urlparse.unquote(url)


def base64_decode(base64string):
    """
    :function base64_code:   decode base 64 encoded string
    :param base64string:     base 64 encoded string
    :return:                 decoded string
    """
    return base64.b64decode(base64string)


def base64_encode(whateverstring):
    """
    :function base64_encode: encode string using base 64 encoding
    :param whateverstring:   simple string
    :return:                 base 64 encoded string previously utf8 encoded
    """
    return base64.b64encode(bytes(whateverstring, 'utf8'))


def decode_saml(samlstring):
    """
    :function decode_saml: decode saml by doing url unquoting, base 64 decoding and decompression
    :param samlstring:     encoded saml string
    :return:               decoded saml string
    """
    urldecodedsaml = urlparse.unquote(samlstring)
    urldecodedsamlplus = urldecodedsaml + '==='
    decodedsamlbytes = base64.b64decode(urldecodedsamlplus.encode('utf8'))

    # can be only b64 encoded and not compressed
    try:
        # the input must include a zlib header and trailer
        samldecompressed = zlib.decompress(decodedsamlbytes, +15)
    except zlib.error:
        try:
            # Uses the absolute value of wbits as the window size logarithm.
            # The input must be a raw stream with no header or trailer.
            samldecompressed = zlib.decompress(decodedsamlbytes, -15)
        except zlib.error:
            print('Decompression failed, only zlib compressed data with ou without headers are accepted.')
            samldecompressed = None

    decodedstring = samldecompressed.decode('utf8')
    return decodedstring


def encode_saml(samlstring):
    """
    :function encode_saml: encode saml by doing compression, base 64 encoding and url quoting
    :param samlString:     saml like string
    :return:               encoded saml string
    """
    samlbyteslike = samlstring.encode('utf8')
    samlcompressed = zlib.compress(samlbyteslike)
    encodedsamlbytes = base64.b64encode(samlcompressed)
    encodedsaml = encodedsamlbytes.decode('utf8')
    urlencodedsaml = urlparse.quote(encodedsaml)
    return urlencodedsaml


def read_from_file(filepath):
    """
    :function read_from_file: read the content of file and remove carriage return
    :param filePath:          file path with file name
    :return: samlText         content of file
    """
    samltext = ""
    # check existing file
    try:
        with open(filepath, "r") as exf:
            for line in exf:
                samltext += line.rstrip("\n")
    except FileNotFoundError:
        print("Wrong file or file path!")
        exit(1)
    return samltext

def main():
    printablereturn = ''
    parser = argparse.ArgumentParser(description="Python tool helping to decode/encode url, base64 and saml strings.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--infile", type=str, help="file path", dest='filename')
    group.add_argument("--instr", type=str, help='str input data', dest='content')

    parser.add_argument("function", help="requested function", choices=["url_decode", "url_encode", "base64_decode",
                                                                        "base64_encode", "saml_decode", "saml_encode"])
    args = parser.parse_args()

    if args.filename is not None:
        content = read_from_file(args.filename)
    elif args.content is not None:
        content = args.content
    else:
        print('An input is needed!')
        exit(1)

    if args.function == 'url_decode':
        printablereturn = url_decode(content)
    elif args.function == 'url_encode':
        printablereturn = url_encode(content)
    elif args.function == 'base64_decode':
        printablereturn = base64_decode(content)
    elif args.function == 'base64_encode':
        printablereturn = base64_encode(content)
    elif args.function == 'saml_decode':
        printablereturn = decode_saml(content)
    elif args.function == 'saml_encode':
        printablereturn = encode_saml(content)

    print(printablereturn)


if __name__ == "__main__":
    main()

