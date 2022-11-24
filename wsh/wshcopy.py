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
    # If "version" arg is set, print version and exit :
    if args.version:
        version = pkg_resources.require("webssh-sh")[0].version
        print("webssh-sh %s" % version)
        exit(0)
    input_content = read_stdin()
    if input_content == "":
        exit(0)
    write_osc52_sequence(input_content)


def read_stdin():
    input_content = ""
    try:
        for line in sys.stdin:
            if '\D' == line.rstrip():
                break
            input_content += line
        input_content = input_content.rstrip()
    except KeyboardInterrupt:
        input_content = ""
    return input_content


def write_osc52_sequence(input_content):
    write_osc52_sequence_start()
    input_content_bytes = input_content.encode("utf-8")
    base64_bytes = base64.b64encode(input_content_bytes)
    base64_string = base64_bytes.decode("utf-8")
    if is_screen():
        """
        => https://github.com/aymanbagabas/go-osc52/blob/64534a3e8e1c38973b62289e51553bafaf52d60c/osc52.go#L181
        Screen doesn't support OSC52 but will pass the contents of a DCS sequence to
                the outer terminal unchanged.

                Here, we split the encoded string into 76 bytes chunks and then join the
                chunks with <end-dsc><start-dsc> sequences. Finally, wrap the whole thing in
                <start-dsc><start-osc52><joined-chunks><end-osc52><end-dsc>.
        """
        s = [base64_string[i:i+76] for i in range(0, len(base64_string), 76)]
        write_stdout("\x1b\\\x1bP".join(s))
    else:
        write_stdout(base64_string)
    write_osc52_sequence_end()


def write_osc52_sequence_start():
    if is_tmux():
        write_stdout("\x1bPtmux;\x1b")
    if is_screen():
        write_stdout("\x1bP")
    write_stdout("\x1b]52;c;")  # OSC52 Sequence Start


def write_osc52_sequence_end():
    write_stdout("\x07")  # OSC52 Sequence End
    if is_tmux():
        write_stdout("\x1b\\")
    if is_screen():
        write_stdout("\x1b\x5c")


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
    if 'TERM' in os.environ and os.environ['TERM'] == "screen" \
            and 'TMUX' not in os.environ:
        return True
    return False


if __name__ == "__main__":
    # Launch the cli :
    cli()
