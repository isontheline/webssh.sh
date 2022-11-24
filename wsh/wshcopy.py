#!/usr/bin/python3
# Author: Arnaud MENGUS / @isontheline
#
# This script will let you copy text from your terminal to your clipboard
# Inspired (a lot) by : https://github.com/aymanbagabas/go-osc52/blob/master/osc52.go
#
# Usage: echo "Hello World" | wshcopy.py
# Usage: wshcopy.py < file.txt
#
# tmux >= 3.3 : set -g allow-passthrough on

import os
import sys
import base64
import argparse
import pkg_resources

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--terminal",
                    help="Force terminal type instead of auto detection", default="auto")
parser.add_argument("-v", "--version",
                    help="Show version of wshcopy", action="store_true")
args = parser.parse_args()

terminal = args.terminal


def cli():
    input_content = ""

    for line in sys.stdin:
        if '\D' == line.rstrip():
            break
        input_content += line

    input_content = input_content.rstrip()

    write_sequence_start()
    write_sequence(input_content)
    write_sequence_end()


def write_sequence(input_content):
    input_content_bytes = input_content.encode("utf-8")
    base64_bytes = base64.b64encode(input_content_bytes)
    base64_string = base64_bytes.decode("utf-8")
    write_stdout("\033]52;c;" + base64_string + "\a")


def write_sequence_start():
    if is_tmux():
        write_stdout("\033Ptmux;\033")


def write_sequence_end():
    if is_tmux():
        write_stdout("\033\\")


def write_stdout(content):
    sys.stdout.write(content)
    sys.stdout.flush()


def is_tmux():
    if terminal == "tmux":
        return True
    if terminal != "auto":
        return False
    if 'TMUX' in os.environ and os.environ['TMUX'] != "":
        return True
    return False


def is_screen():
    if terminal == "screen":
        return True
    if terminal != "auto":
        return False
    if 'TERM' in os.environ and os.environ['TERM'] == "screen":
        return True
    return False


if __name__ == "__main__":
    # If "version" arg is set, print version and exit :
    if args.version:
        version = pkg_resources.require("webssh-sh")[0].version
        print("webssh-sh %s" % version)
        exit(0)

    # Launch the cli :
    cli()
