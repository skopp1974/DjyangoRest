import sys
import os
import os.path
from os import path
import csv
import pandas

rawdat_files_location = sys.path[0] + "\\RawData"
print('Raw data file location: ' + rawdat_files_location)

print ("file exist:"+str(path.exists(rawdat_files_location)))

def validate_raw_data(db_record):
    RetVal = False
    raw_data_file_from_db = db_record['raw_data_file']
    try:
        RetVal = path.exists(raw_data_file_from_db)
    except FileNotFoundError:
        print('validate_raw_data: FileNotFoundError for {}'.format(raw_data_file_from_db))
    else:
        #Raw File exists. Now validate metadata
        colnames = ['id', 'well_name', 'rig_location', 'well_depth']
        data = pandas.read_csv(raw_data_file_from_db, names=colnames)

        # Group list of each radata field so the serach can be done easily for any number of records in CSV
        ids = data.id.tolist()
        well_names = data.well_name.tolist()
        rig_locations = data.rig_location.tolist()
        well_depths = data.well_depth.tolist()

        if ids.count(str(db_record['id'])) and \
            well_names.count(db_record['well_name']) and \
            rig_locations.count(db_record['rig_location']) and \
            well_depths.count(str(db_record['well_depth'])):
            RetVal = True
        else:
            RetVal = False
            
    if RetVal:
        print('Meta Data validation success for record ID [{0}]: SUCCESS'.format(db_record['id']))
    else:
        print('Meta Data validation success for record ID [{0}]: FAILED'.format(db_record['id']))
    
    return RetVal

