import json
import requests
from schemavalidator import validate_rig

# read file
with open("c:\\Users\\srinik\\RestTest\\DJango\\RestInjestion2\\RestInj2\\RigTest\\manifest.json", "r") as manifest:
    jsondata = manifest.read()
    manifest_data = json.loads(jsondata)

json_from_db = requests.get(manifest_data["GetDataFromRestEndPoint"])

if json_from_db.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /rigs/ {}'.format(resp.status_code))

db_json = json_from_db.json()

print("================= RECORDS FROM DATABASE ====================")
print(json.dumps(db_json, sort_keys=True, indent=4))
print("================= RECORDS FROM DATABASE ====================")

for each_rig in db_json:
    print(validate_rig(each_rig))
#print(json.dumps(manifest_data, sort_keys=True, indent=4))




# #prompt the user for a file to import
# filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
# filename = rs.OpenFileName("Open JSON File", filter)

# #Read JSON data into the datastore variable
# if filename:
#     with open(filename, 'r') as f:
#         datastore = json.load(f)

# #Use the new datastore datastructure
# #sprint datastore["office"]["parking"]["style"]