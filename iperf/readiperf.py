import json
from fastavro import reader, parse_schema
import sys

with open('test_outputu.avro', 'rb') as infile:
    for record in reader(infile):
        print(json.dumps(record, indent=4))

