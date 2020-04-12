# gen_doc.py: generate python and markdown docs for python modules


function : gen_pymddoc
------
```
Call write methods from module path in order to generate module documentation

:param modulepath: module path
:type modulepath:  str
:return:           python md documentation path
:rtype:            str
```
function : get_modulename
------
```
Get the name of a module from the module path

:param path: path of the module file
:type path:  str
:return:     module name without file extension
:rtype:      str
```
function : import_mod
------
```
Import module from name

:param modulename: name of the module to import
:type modulename:  str
:return:           a module
:rtype:            class module
```
function : import_module
------
```
Import a module.

The 'package' argument is required when performing a relative import. It
specifies the package to use as the anchor point from which to resolve the
relative import to an absolute import.
```
function : main
------
```
main function - execute only if run as a script

description: degenerate python and markdown doc into local working directory file
```
function : write_markdownform
------
```
Write markdown documentation from python doc contained into a module

:param module: python module
:type module:  class module
:return:       markdown documentation
:rtype:        str
```
function : write_to_file
------
```
Write content to file into working directory

:param filename: name of file containing extension
:type filename:  str
:param content:  text
:type content:   str
:return:         file path
:rtype:          str
```
