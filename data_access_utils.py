# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:04:33 2022

@author: Ryan
"""

#import pymongo
#from pymongo import MongoClient
import pandas as pd
import requests
import json
from datetime import datetime, timezone, timedelta
import subprocess
import dotenv
import os


os.chdir('C:/Users/Ryan/Documents/GitHub/cgm-glucose-modeling/')
dotenv.load_dotenv('./.env')


def ping_mongodb_for_sensor_entries():
    url = "https://data.mongodb-api.com/app/data-bubgl/endpoint/data/v1/action/find"
    payload = json.dumps({
        "collection": "entries",
        "database": os.getenv('MONGODB_DATABASE_NAME'),
        "dataSource": "Cluster0"
    })
    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': os.getenv('API_KEY'),
    }
    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=payload)
    
    entries_json = json.loads(response.text)
    entries_df = pd.DataFrame(entries_json['documents'])
    entries_df.sort_values(by=['date'],
                           inplace=True,
                           ascending=False)
    
    # unix timestamp in 'date' element comes in milliseconds, must be converted to seconds
    last_record_datetime = datetime.fromtimestamp(entries_df['date'].max()/1000,
                                                  timezone(offset=-timedelta(hours=6)))
    now_datetime = datetime.now(timezone(offset=-timedelta(hours=6)))
    time_since_last_record = now_datetime - last_record_datetime
    mins_since_last_record = time_since_last_record.seconds/60
    return mins_since_last_record


def backup_mongodb_data(mongoexport_exe_fileloc="C:/Program Files/MongoDB/Tools/100/bin/"):
    # Backup mongodb records
    result_int = subprocess.run([f"{mongoexport_exe_fileloc}mongoexport.exe",
                                 f'--uri={os.getenv("MONGODB_DATAEXPORT_URI")}',
                                 '--collection',
                                 'entries',
                                 '--type=json',
                                 '--out',
                                 './Nightscout_Backups/backup.json'])
    
    if result_int != 0:
        print('The backup export was not completed successfully.')
    return result_int
    