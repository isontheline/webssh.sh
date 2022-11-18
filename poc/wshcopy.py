#!/usr/bin/python3
import base64

input_content = input()
input_content_bytes = input_content.encode("ascii")

base64_bytes = base64.b64encode(input_content_bytes)
base64_string = base64_bytes.decode("ascii")

print("\033]52;c;" + base64_string +  "\a", end='\r')