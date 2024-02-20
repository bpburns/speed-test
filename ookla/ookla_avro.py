from fastavro import parse_schema, writer, reader
import json

with open('schema/ookla_result.avsc', 'r') as infile:
    parsed_schema = parse_schema(json.loads(infile.read()))

with open('sample_ookla_result.json', 'r') as infile:
    json_record = json.loads(infile.read())

with open('test_output.avro', 'wb') as outfile:
    writer(outfile, parsed_schema, [json_record])

with open('test_output.avro', 'rb') as infile:
    loaded_records = reader(infile)
    for r in loaded_records:
        print(json.dumps(r, indent=4))

