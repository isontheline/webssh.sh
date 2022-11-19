#!/usr/bin/python3

import base64
import sys


def cli():
    input_content = ""

    for line in sys.stdin:
        if '\D' == line.rstrip():
            break
        input_content += line

    input_content = input_content.rstrip()
    input_content_bytes = input_content.encode("utf-8")

    base64_bytes = base64.b64encode(input_content_bytes)
    base64_string = base64_bytes.decode("utf-8")

    print("\033]52;c;" + base64_string + "\a", end='\r')

if __name__ == "__main__":
    cli()