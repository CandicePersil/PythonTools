# PythonTools
It contains helping pythons scripts

* decode_tool
* gen_doc

# gen_doc.py

* description

Creation of a markdown file containing the python documentation of an input module.

* module usage
    * import module in python CLI
    ```
    import gen_doc
  
    gen_doc.gen_pymddoc("/path/modulename.py")
    ```
    * use module as python script
    ```
    > gen_doc.py "/path/modulename.py"
    ```

Generation of python doc file (md format) in working directory - 
Creation of ./modulename.py.

* script usage help
```
usage: gen_doc.py [-h] modulepath

...

positional arguments:
  modulepath  Module path

optional arguments:
  -h, --help  show this help message and exit
```

# decode_tool.py

* description

It contains decoding and encoding python methods.

* module usage
    * import module in python CLI
    ```
    >>> import decode_tool
    >>> decode_tool.url_encode("http://url_to_encode&and_thats_it.com")
    'http%3A//url_to_encode%26and_thats_it.com'
    ```
    * use module as python script
    ```
    > python decode_tool.py url_encode --instr "https://www.google.com/search?q=url+to+encode&oq=url+to+encode"
    https%3A//www.google.com/search%3Fq%3Durl%2Bto%2Bencode%26oq%3Durl%2Bto%2Bencode
    ```

* script usage help
```
usage: decode_tool.py [-h] [--infile FILENAME | --instr CONTENT] {url_decode,url_encode,base64_decode,base64_encode,saml_decode,saml_encode}

Python tool helping to decode/encode url, base64 and saml strings.

positional arguments:
  {url_decode,url_encode,base64_decode,base64_encode,saml_decode,saml_encode}
                        requested function

optional arguments:
  -h, --help            show this help message and exit
  --infile FILENAME     file path
  --instr CONTENT       str input data
```

### Decode and encode examples 

#### execution from python CLI

<em> (have fun using subprocess module)</em>

* url_encode
```
>import subprocess
    
>subprocess.call(['python', 'decode_tool.py', '--instr', 'https://toto:titi:tata&tutu.com', 'url_encode'])

https%3A//toto%3Atiti%3Atata%26tutu.com
```

* url_decode
```
>subprocess.call(['python', 'decode_tool.py', '--instr', 'https%3A//toto%3Atiti%3Atata%26tutu.com', 'url_decode'])

https://toto:titi:tata&tutu.com
```
* saml_encode
```
>subprocess.call(['python', 'decode_tool.py', '--infile', '.test_files/saml_ex.txt', 'saml_encode'])

eJzFVllv4zYQ/iuC3m1R94FErZu0hYFcjYNF0ZeAIodrFrogUrD77ztSJEdWstpsW2wBA5bm/r7hDHWhaJHXySOouioVGMciL1XSCy/NtimTiiqpkpIWoBLNkt3m9iZx1iSpm0pXrMrNicuyB1UKGi2r0jS215fmcwQRZ74IYhpHjHnMFsL1nBB8Bq4XkEDwIHREbENgGp%2BgUeh5aWIgdFeqhW2pNC01iojtrUi4ssMnYif486I/TOMalJYl1b3XXus6sSxVr%2BFIizqHNasKi0NR2ZYsORzX9b7%2BgTKFscuRi6fq0ry/%2B/nm/tft3bMnANyMeIEb%2B8yD0LeJbUMciigmJPOd0OV%2BEES%2BmRrGRcdF0hfZpENqyc9zF6App5p2iS%2BsqcPgXyc7TXWr8H0muao4GJ9o3sIy36q3TnYtY6CUaXWRrVnol1I3Y2eGXh6VPHF2OBzWB3ddNZ8thxDb%2Bv32Zsf2UNCV7BvAwDx5fd1paD0PberSCGKBjfdZDDF3vAhESLzYjV3BIkE88EXo/4PWvzL2L3owRti12Z/AdC8ZZXdI9fba2D10D7%2B1NJdCQrN8yqa5TOOXqimoXm5fJ5F8JXrTRDe0VBJKbabPOB/cib0o85joGAg4AKEkczkPcJyygIkIHxweDqheCj7DMOC6qkohuwRd829B7yu%2BXBUrkgxoA405hFsIeI14jbtK35f3zUbojiKHONgwe2VHTyRInGFWH4HJugP3XSfVGgmxvgQgfaueHA205LIzUx3InwA7Be8cSbtD%2BAEWztqzaTnywQAR6kayUzFvLdKPnroBx8nvDPyX8g3qV6jptAK9L7tNAgW2zuhfv7KUd7iIMMp7bLyYxnPTbddz3BgZxHEQ0ozHxOOcUXAZgcyzo5jyDFwR2uA6IROxOycSq8LyNRz1GwZfVVc53k6PINLFC4wlrLND8QP%2BHaqGn%2Bh7J9SM4FkdU/mJxCm7GhuRtRrOlW/URjfcOLOSm/3jR1YLRedOOi6XDO3YfKBPGfqrxsA7IdF/1ZjqiJc9qsrPZqrxuIxAzsxn4EfdIoSCyvx/wvDjZHT%2BMzzA2we8u6pyI4TMJX359Pnu%2BFq829USqG8JNvDUVDnY30zUXDg92aNu/BJJx0%2BVccenfwOixoQj
```

* saml_decode
```
>subprocess.call(['python', 'decode_tool.py', '--infile', './encoded_saml_ex.txt', 'saml_decode'])
	
	<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" ID="_8e8dc5f69a98cc4c1ff3427e5ce34606fd672f91e6" Version="2.0" IssueInstant="2014-07-17T01:01:48Z" Destination="http://sp.example.com/demo1/index.php?acs" InResponseTo="ONELOGIN_4fee3b046395c4e751011e97f8900b5273d56685">
	  <saml:Issuer>http://idp.example.com/metadata.php</saml:Issuer>
	  <samlp:Status>
		<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
	  </samlp:Status>
	  <saml:Assertion xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xs="http://www.w3.org/2001/XMLSchema" ID="_d71a3a8e9fcc45c9e9d248ef7049393fc8f04e5f75" Version="2.0" IssueInstant="2014-07-17T01:01:48Z">
		<saml:Issuer>http://idp.example.com/metadata.php</saml:Issuer>
		<saml:Subject>
		  <saml:NameID SPNameQualifier="http://sp.example.com/demo1/metadata.php" Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient">_ce3d2948b4cf20146dee0a0b3dd6f69b6cf86f62d7</saml:NameID>
		  <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
			<saml:SubjectConfirmationData NotOnOrAfter="2024-01-18T06:21:48Z" Recipient="http://sp.example.com/demo1/index.php?acs" InResponseTo="ONELOGIN_4fee3b046395c4e751011e97f8900b5273d56685"/>
		  </saml:SubjectConfirmation>
		</saml:Subject>
		<saml:Conditions NotBefore="2014-07-17T01:01:18Z" NotOnOrAfter="2024-01-18T06:21:48Z">
		  <saml:AudienceRestriction>
			<saml:Audience>http://sp.example.com/demo1/metadata.php</saml:Audience>
		  </saml:AudienceRestriction>
		</saml:Conditions>
		<saml:AuthnStatement AuthnInstant="2014-07-17T01:01:48Z" SessionNotOnOrAfter="2024-07-17T09:01:48Z" SessionIndex="_be9967abd904ddcae3c0eb4189adbe3f71e327cf93">
		  <saml:AuthnContext>
			<saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</saml:AuthnContextClassRef>
		  </saml:AuthnContext>
		</saml:AuthnStatement>
		<saml:AttributeStatement>
		  <saml:Attribute Name="uid" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
			<saml:AttributeValue xsi:type="xs:string">test</saml:AttributeValue>
		  </saml:Attribute>
		  <saml:Attribute Name="mail" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
			<saml:AttributeValue xsi:type="xs:string">test@example.com</saml:AttributeValue>
		  </saml:Attribute>
		  <saml:Attribute Name="eduPersonAffiliation" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
			<saml:AttributeValue xsi:type="xs:string">users</saml:AttributeValue>
			<saml:AttributeValue xsi:type="xs:string">examplerole1</saml:AttributeValue>
		  </saml:Attribute>
		</saml:AttributeStatement>
	  </saml:Assertion>
	</samlp:Response>
```
