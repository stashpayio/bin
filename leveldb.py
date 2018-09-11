#!/usr/bin/env python
import sys
import plyvel

def convertToHex(str):
    return ''.join(x.encode('hex') for x in str)

db = plyvel.DB(sys.argv[1])
count = 1
for key,value in db:
    #print(type(key))
    if len(key) < 100:
    	print(key) 
        print(convertToHex(value)
    count+=1
print(count)
db.close()

