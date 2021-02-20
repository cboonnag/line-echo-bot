import json
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__))) 

#open JSON file 
with open("../config.json") as f: 
    data = json.load(f)\
    
    CHANNEL_SECRET = data['line_config'][0]['CHANNEL_SECRET']
    CHANNEL_ACCESS_TOKEN = data['line_config'][0]['CHANNEL_ACCESS_TOKEN']
    BASIC_ID = data['line_config'][0]['BASIC_ID']
    f.close()