# example usage: python fromjson.py sample.json sampleout.txt
#sample.json is the file to read from
#sampleout.txt is the file to write to


import json
import sys

def read_json(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":

    file1 = str(sys.argv[1]) if (len(sys.argv)>1) else "sample.json"
    file2 = str(sys.argv[2]) if (len(sys.argv)>2) else "sampleout.txt"

    data = read_json(file1)

    with open(file2, "w") as f:
        for value in data.values():
            f.write(str(value) + '\n')