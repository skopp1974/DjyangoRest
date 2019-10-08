import json
from jsonschema import validate
import sys, os

# print('sys.argv[0] =', sys.argv[0])             
# pathname = os.path.dirname(sys.argv[0])        
# print('path =', pathname)
# print('full path =', os.path.abspath(pathname)) 

schema_file_with_path = sys.path[0] +"\\rigschema.json"


#For testing only
#schema_file_with_path = sys.path[0] +"\\simpleschema.json"

print("Schema File Path: " + schema_file_with_path)



# read file
with open(schema_file_with_path, "r") as schema:
    filebuf = schema.read()
jsonschema = json.loads(filebuf)

print(jsonschema)
    #manifest_data = json.loads(jsondata)

# Only for testing to override file read
# jsonschema = {
#     "type": "object",
#     "properties": {
#         "price": {"type": "number"},
#         "name": {"type": "string"},
#     },
# }
###

test_record_json = {
    "id":"1",
    "rig_name": "HoustonRig",
    "rig_location": "Houston",
    "well_bore_diameter": "100",
    "well_name": "well1", 
    "well_location": "Houston",
    "well_diameter": "90",
    "well_depth": "1000",
    "raw_data": "c:\\Users\\srinik\\RestTest\\DJango\\RestInjestion2\\RestInj2\\RigTest\\RawData\\1.dat"
}

#Testing override
#test_record_json2 = {"name" : "Eggs", "price" : 1}


def validate_rig(db_record):
    retval = True
    try:
        validate(instance=db_record, schema=jsonschema)
    except:
        print("Schema validation failed")
        retval = False
    return retval

# UNIT Test
print(validate_rig(test_record_json))