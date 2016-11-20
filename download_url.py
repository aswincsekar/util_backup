import sys
import os
import urllib

print "system arguments"
print sys.argv

base_path = os.path.dirname(os.path.abspath(__file__))
print "base_path: " + base_path

filename = sys.argv[1]
filepath = os.path.join(base_path, filename)
print "filepath: "+filepath

with open(filepath, 'r') as file:
    for line in file:
        print line,
        imagename = line.split("/")[-1]
        imagepath = os.path.join(base_path, 'images', imagename)
        print(imagepath)
        try:
            urllib.urlretrieve(line, imagepath)
        except:
            print "Error"
            pass
