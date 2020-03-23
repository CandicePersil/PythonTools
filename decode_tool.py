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


def base64_deçode(base64String):
    """
    :function base64_çode: decode base 64 encoded string
    :param base64String:     base 64 encoded string
    :return:                 decoded string
    """
    return base64.b64decode(base64String)


def base64_encode(whateverString):
    """
    :function base64_encode: encode string using base 64 encoding
    :param whateverString:   simple string
    :return:                 base 64 encoded string
    """
    return base64.b64encode(whateverString)


def decode_saml(samlString):
    """
    :function decode_saml: decode saml by doing url unquoting, base 64 decoding and decompression
    :param samlString:     encoded saml string
    :return:               decoded saml string
    """
    urlDecodedSaml = urlparse.unquote(samlString)
    urlDecodedSamlPlus = urlDecodedSaml + '==='
    decodedSamlBytes = base64.b64decode(urlDecodedSamlPlus.encode('utf8'))

    # can be only b64 encoded and not compressed
    try:
        # the input must include a zlib header and trailer
        samlDecompressed = zlib.decompress(decodedSamlBytes, +15)
    except zlib.error:
        try:
            # Uses the absolute value of wbits as the window size logarithm.
            # The input must be a raw stream with no header or trailer.
            samlDecompressed = zlib.decompress(decodedSamlBytes, -15)
        except zlib.error:
            print('Decompression failed, only zlib compressed data with ou without headers are accepted.')
            samlDecompressed = None

    decodedString = samlDecompressed.decode('utf8')
    return decodedString


def encode_saml(samlString):
    """
    :function encode_saml: encode saml by doing compression, base 64 encoding and url quoting
    :param samlString:     saml like string
    :return:               encoded saml string
    """
    samlBytesLike = samlString.encode('utf8')
    samlCompressed = zlib.compress(samlBytesLike)
    encodedSamlBytes = base64.b64encode(samlCompressed)
    encodedSaml = encodedSamlBytes.decode('utf8')
    urlEncodedSaml = urlparse.quote(encodedSaml)
    return urlEncodedSaml


def read_from_file(filePath):
    """
    :function read_from_file: read the content of file and remove carriage return
    :param filePath:          file path with file name
    :return: samlText         content of file
    """
    samlText = ""
    # check existing file
    try:
        with open(filePath, "r") as exf:
            for line in exf:
                samlText += line.rstrip("\n")
    except FileNotFoundError:
        print("Wrong file or file path!")
        exit(1)
    return samlText

def main():
    content = ''
    printableReturn = ''
    parser = argparse.ArgumentParser(description="Python tool helping to decode/encode url, base64 and saml strings.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--infile", type=str, help="file path", dest='fileName')
    group.add_argument("--instr", type=str, help='str input data', dest='content')

    parser.add_argument("function", help="requested function", choices=["url_decode", "url_encode", "base64_decode",
                                                                        "base64_encode", "saml_decode", "saml_encode"])
    args = parser.parse_args()

    if args.fileName is not None:
        content = read_from_file(args.fileName)
    elif args.content is not None:
        content = args.content
    else:
        print('An input is needed!')
        exit(1)

    if args.function == 'url_decode':
        printableReturn = url_decode(content)
    elif args.function == 'url_encode':
        printableReturn = url_encode(content)
    elif args.function == 'base64_decode':
        printableReturn = base64_deçode(content)
    elif args.function == 'base64_encode':
        printableReturn = base64_deçode(content)
    elif args.function == 'saml_decode':
        printableReturn = decode_saml(content)
    elif args.function == 'saml_encode':
        printableReturn = encode_saml(content)

    print(printableReturn)


if __name__ == "__main__":
    main()

