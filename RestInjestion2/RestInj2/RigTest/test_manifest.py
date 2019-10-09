import json
import requests
from schemavalidator import validate_rig
from rawdatavalidator import validate_raw_data


# read manifest file
# Send web request and get records in JSON
with open("c:\\Users\\srinik\\RestTest\\DJango\\RestInjestion2\\RestInj2\\RigTest\\manifest.json", "r") as manifest:
    jsondata = manifest.read()
    manifest_data = json.loads(jsondata)

# Send web request
json_from_db = requests.get(manifest_data["GetDataFromRestEndPoint"])
if json_from_db.status_code != 200:
    raise ApiError('GET /rigs/ {}'.format(resp.status_code))

#Records in JSON
db_json = json_from_db.json()

print("================= RECORDS FROM DATABASE ====================")
print(json.dumps(db_json, sort_keys=True, indent=4))
print("============================================================\n")

def test_validate_rig():
    for each_rig in db_json:
        # Check Data model schema
        ret = validate_rig(each_rig)
        assert ret == True

def test_validate_raw_data():
    for each_rig in db_json:
        # Check Data model schema
        ret = validate_raw_data(each_rig)
        assert ret == True


# Perform data validation
print("================= DATA VALIDATION REPORT ====================\n")
for each_rig in db_json:
    # Check Data model schema
    validate_rig(each_rig)
    
    # Check for raw data integrity.
    validate_raw_data(each_rig)
    print('')
print("=============================================================")

