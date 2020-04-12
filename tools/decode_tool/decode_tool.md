# decode_tool.py: Encode and decode strings


function : base64_decode
------
```:function base64_code:   decode base 64 encoded string:

:param base64string:     base 64 encoded string
:return:                 decoded string
```
function : base64_encode
------
```:function base64_encode: encode string using base 64 encoding:

:param whateverstring:   simple string
:return:                 base 64 encoded string previously utf8 encoded
```
function : decode_saml
------
```:function decode_saml: decode saml by doing url unquoting, base 64 decoding and decompression:

:param samlstring:     encoded saml string
:return:               decoded saml string
```
function : encode_saml
------
```:function encode_saml: encode saml by doing compression, base 64 encoding and url quoting:

:param samlString:     saml like string
:return:               encoded saml string
```
function : main
------
```:main function:
:description:   Python tool helping to decode/encode url, base64 and saml strings:

:functions:     base64, url, and saml encode and decode:
:inputs:        strings, file:

:return:        none
```
function : read_from_file
------
```:function read_from_file: read the content of file and remove carriage return:

:param filePath:          file path with file name
:return: samlText         content of file
```
function : url_decode
------
```:function url_decode: decode url encoded string:

:param url:           url or query string
:return:              decoded url/query encoded string
```
function : url_encode
------
```:function url_encode: encode string:

:param url:           url or query string
:return:              encoded url/query string
```
