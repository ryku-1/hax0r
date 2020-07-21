#!usr/bin/python3

#tool for extracting js filenames from access.logs

import re
import sys

filenames = set()

with open(sys.argv[-1]) as i:
        for line in i:
                end = line.rfind(".js") + 3
                start = line.rfind("/", 0, end) + 1
                filename = line[start:end]
                if filename.endswith(".js"):
                        filenames.add(filename)


for filename in sorted(filenames, key=str.lower):
        print(filename)
