#!/usr/bin/env python3
import sys

fname = sys.argv[1]
verse = int(sys.argv[2])

fin = open(fname, "r")
line = fin.readline()
out = []

while line:
  out.append(str(verse) + "^" + line)
  verse = verse + 1
  line = fin.readline()

fin.close()

for line in out:
  print(line, end="")
