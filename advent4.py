#!/usr/bin/python
import hashlib

m = hashlib.md5()
puzzle_input='ckczppom'
i=0

while True:
    if hashlib.md5(puzzle_input+str(i)).hexdigest()[0:6] == '000000':
        print i
        break
    i+=1
