import json
from jsonschema import validate
import sys
import os

schema_file_with_path = sys.path[0] + "\\rigschema.json"

# For testing only
#schema_file_with_path = sys.path[0] +"\\simpleschema.json"

print("Schema File Path: " + schema_file_with_path)

# read file
with open(schema_file_with_path, "r") as schema:
    filebuf = schema.read()
jsonschema = json.loads(filebuf)

#Validate schema
def validate_rig(db_record):
    retval = True

    try:
        validate(instance=db_record, schema=jsonschema)
    except:
        retval = False

    if retval:
        print('JSON Schema validation for record ID [{0}]: SUCCESS'.format(db_record['id']))
    else:
        print('JSON Schema validation for record ID [{0}]: FAILED'.format(db_record['id']))

    return retval