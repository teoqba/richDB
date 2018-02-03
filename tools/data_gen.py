#!/usr/bin/env python

import json

rims_array = [{'brand': 'Enve', 'holes': 32, 'name': 'Enve m60'},
{'brand': 'Enve', 'holes': 24, 'name': 'Enve m50'},
{'brand': 'Enve', 'holes': 32, 'name': 'Enve m50'},
{'brand': 'Enve', 'holes': 32, 'name': 'Enve m60'},
{'brand': 'Dt Swiss', 'holes': 24, 'name': 'XM 320'},
{'brand': 'Dt Swiss', 'holes': 32, 'name': 'XT 500'},
{'brand': 'Dt Swiss', 'holes': 32, 'name': 'AR 122'},
{'brand': 'Dt Swiss', 'holes': 24, 'name': 'XT 500'},
{'brand': 'Dt Swiss', 'holes': 32, 'name': 'EX 551'},
{'brand': 'Derby', 'holes': 32, 'name': 'Derby XC'},
{'brand': 'Derby', 'holes': 32, 'name': 'Derby AM'},
{'brand': 'Derby', 'holes': 32, 'name': 'Derby DH'}]

hubs_array=[{'brand':'DTSwiss', 'name':'DTSwis 350', 'type':'front', 'axle':'15mm', 'disc':'iso', 'spoke':32},
     {'brand':'DTSwiss', 'name':'DTSwis 350', 'type':'rear', 'axle':'15mm', 'disc':'iso', 'spoke':32},
     {'brand':'DTSwiss', 'name':'DTSwis 350', 'type':'rear', 'axle':'15mm', 'disc':'iso', 'spoke':24},
     {'brand':'DTSwiss', 'name':'DTSwis 350', 'type':'front', 'axle':'15mm', 'disc':'iso', 'spoke':24}]


rims = {}
hubs = {}
for i,rim in enumerate(rims_array):
    rims[i] = rim

for i,hub in enumerate(hubs_array):
    hubs[i] = hub

data  = {'rims':rims, 'hubs':hubs}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)