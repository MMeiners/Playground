#! /usr/bin/env python3.8-64
# Purpose: say hello

import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('-n', '--name', default='World', metavar='name', help='Name to greet')
args = parser.parse_args()

print(f'Hello, {args.name}!')
