#!/usr/bin/python3
"""
Script to turn on all lights specified into 'lights.json' file
"""

import sys
import json,requests
import configparser



if __name__ == '__main__':

    #default state is OFF
    state = 'off'
    try:
        arg = sys.argv[1]
        arg=arg.lower()
        if 'on' == arg:state ='on'
    except:
        print("ERROR - missing on/off state parameter")
        exit()

    #get my lights entity_ids
    lights_inv = json.loads(open("lights.json").read())

    #get my token
    config = configparser.ConfigParser()
    config.read('config.ini')

    #turn on all lights

    for i in range (len(lights_inv)+1):
        headers = {
            "Authorization": "Bearer " + str(config['Account']['gb_token']),
            "content-type": "application/json",
            "Access - Control - Allow - Origin": "*"
            }
        data = {"entity_id":lights_inv["hlights"][i]["entity_id"]}
        url = "http://homeassistant.goldenbyte.it:8123/api/services/light/turn_"+state
        data=json.dumps(data)
        responce = requests.post(url,data=data,headers=headers)
        print(responce)
