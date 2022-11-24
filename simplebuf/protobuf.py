# protoc -I=. --python_out=. ./options.proto  

import os
import subprocess
import importlib
import sys
import inspect
import time

import json
from .google.protobuf import json_format


def format_str(field : dict, index: int):
    
    pb_types = {
        'str'   : 'string',
        'int'   : 'int64',
        'float' : 'double',
    }

    return f'{pb_types[field["type"]]} {field["name"]} = {index+1};'

def create(RECORD_NAME: str, REPEATED_NAME: str, FIELDS: str, MESSAGE_NAME="Records"): 

    FIELDS = "\n\t".join([ format_str(record, index) for index, record in enumerate(FIELDS) ])
    template = 'syntax = "proto3";\n\nmessage %s {\n\trepeated %s %s = 1;\n}\n\nmessage %s { \n\t%s\n}\n' % (MESSAGE_NAME, RECORD_NAME, REPEATED_NAME, RECORD_NAME, FIELDS)

    with open(f"{REPEATED_NAME}.proto","w") as f:
        f.write(template)

    return f"{REPEATED_NAME}.proto"

def build(proto_name: str):

    output = subprocess.getoutput([f'protoc -I=. --python_out=. ./{proto_name}'])
    assert output == "", output

    py_name = proto_name.replace(".proto","_pb2.py")
    f = open(py_name,"r")
    new_lines = []
    for line in f.readlines():
        new_line = line.replace("google","simplebuf.google") if "simplebuf" not in line else line
        new_lines.append(new_line)

    f = open(py_name,"w")
    f.writelines(new_lines)

    time.sleep(5)

def validate():
    assert os.name == 'posix', "non-unix OS not supported"

def predict_fields(sample):

    assert type(sample).__name__ == "list" or \
        type(sample).__name__ == "dict", "sample must equal record or list of records!!!"

    sample = sample[0] if type(sample).__name__ == "list" else sample

    fields = []
    for name in sample:

        fields.append({
            "name" : name,
            "type" : type(sample[name]).__name__
        })

    return fields

def generate(RECORD_NAME: str, REPEATED_NAME: str, MESSAGE_NAME: str ="Records", sample: list = []):

    assert sample != [], """Sample is empty!!!"""

    proto_name = create(
        RECORD_NAME, 
        REPEATED_NAME, 
        FIELDS = predict_fields(sample),
        MESSAGE_NAME = MESSAGE_NAME
    )

    build(proto_name)

    return f"{REPEATED_NAME}_pb2"

def recordsToMessage(RECORD_NAME: str, REPEATED_NAME: str, data: list, MESSAGE_NAME="Records"):

    # if not os.path.exists(f"{REPEATED_NAME}.proto") \
    #     or not os.path.exists(f"{REPEATED_NAME}_pb2.py"):
    #         generate(
    #             RECORD_NAME   = RECORD_NAME, 
    #             REPEATED_NAME = REPEATED_NAME, 
    #             MESSAGE_NAME  = MESSAGE_NAME,
    #             sample = data
    #         )

    data = {
        REPEATED_NAME : data
    }

    REPEATED_CLASS = None
    pb_module = importlib.import_module(f"{REPEATED_NAME}_pb2")
    for name, obj in inspect.getmembers(pb_module):
        if MESSAGE_NAME in name:
            REPEATED_CLASS = obj
    
    assert REPEATED_CLASS != None, """problem importing pb "REPEATED" object"""

    string = json.dumps(data)
    message = json_format.Parse(string, REPEATED_CLASS())    

    return message

def messageToDict(msg):
    return json_format.MessageToDict(msg)

def messageToJson(msg):
    return json_format.MessageToJson(msg)