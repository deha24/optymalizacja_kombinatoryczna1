# example usage: python tojson.py sample.json "D~c" "D???c" "N???" "N~~~~"
#sample.json is the file to write to
#the rest are graph6 strings to be written into the json file

import json
import sys

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

    file = str(sys.argv[1]) if (len(sys.argv)>1) else "sample.json"
    
    data = []
    i=2
    while(sys.argv[i:]):
        if data == '':
            continue
        data.append(str(sys.argv[i]))
        i+=1
    print(data)
    write_json(file, data)