#control HA lights from ESP32 and KY-038 module

import json
from machine import ADC,Pin
from urequests import post,get
#from requests import post,get  # requests module not avaiable from ESP32
from time import sleep

def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('my_wifi', 'my_psw')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)

def change_light_state(ha_hentity):
    data = {"entity_id": ha_hentity}  # entity controlled by micropython

    headers = {
        "Authorization": "Bearer " + "HA_TOKEN",
        "content-type": "application/json",
        "Access - Control - Allow - Origin": "*"
    }

    url = "http://homeassistant.mydomain.it:8123/api/states/{}".format(data['entity_id'])

    responce = get(url, headers=headers)
    if responce.status_code == 200:
        results = json.loads(responce.text)
        if results['state'] == 'off':
            new_url = "http://homeassistant.goldenbyte.it:8123/api/services/light/turn_on"
            post(new_url, headers=headers, json=data)
        elif results['state'] == 'on':
            new_url = "http://homeassistant.goldenbyte.it:8123/api/services/light/turn_off"
            post(new_url, headers=headers, json=data)



#Wifi-connect
no_debug()
connect()

pin = 34

pot = ADC(Pin(pin))
pot2 = ADC(Pin(pin))
pot.atten(ADC.ATTN_11DB)  # Full range: 3.3v
while True:
    pot_value = pot.read()
    pot2_value = pot2.read()
    if pot_value == 4095 or pot2_value == 4095:
        print("pot1 = {}  -----  pot2 = {}".format(pot_value,pot2_value))
        print('rilevato')
        change_light_state("light.bedroom")
        sleep(5)    # not listen 4 5 second by last trigger



