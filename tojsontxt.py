# example usage: python tojson.py sample.txt sample.json
#sample.json is the file to write to
#sample.txt is the file to read from

import json
import sys

def read_txt(file):
    data = []
    with open(file, "r") as f:
        for line in f:
            data.append(line.strip())
    return data

def write_json(file, data):
    filelen = 0
    if file:
        filelen = len(read_json(file))

    i=0
    prepare_to_json = read_json(file) if filelen>0 else {}
    prepare_to_json.update(dict(("graph"+str(filelen + i + 1), str(data.pop(0))) for i in range(len(data))))
    json_str = json.dumps(prepare_to_json, indent=4)
    with open(file, "w") as f:
        f.write(json_str)

def read_json(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":

    file_source = str(sys.argv[1]) if (len(sys.argv)>1) else ""
    file_dest = str(sys.argv[2]) if (len(sys.argv)>1) else "sample.json"
    data = read_txt(file_source) if file_source != "" else []
    write_json(file_dest, data)