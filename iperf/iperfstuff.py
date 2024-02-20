import json
from fastavro import writer, parse_schema
import sys

with open('sendu.json', 'r') as infile:
    json_sample = infile.read()
    
with open('iperf_udp_result.avsc', 'r') as infile:
    parsed_schema = parse_schema(json.loads(infile.read()))

# print(json.dumps(parsed_schema, indent=4))

parsed_json = json.loads(json_sample)

print(type(parsed_json))

records = [parsed_json]
print(type(records))
print(dir(records))
print(type(records[0]))


with open('test_outputu.avro', 'wb') as outfile:
    writer(outfile, parsed_schema, records)

