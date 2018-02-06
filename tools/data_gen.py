#!/usr/bin/env python

import json

rims_array = [{'brand': 'Enve', 'spokes': 32, 'name': 'Enve m60'},
{'brand': 'Enve', 'spokes': 24, 'name': 'Enve m50'},
{'brand': 'Enve', 'spokes': 32, 'name': 'Enve m50'},
{'brand': 'Enve', 'spokes': 32, 'name': 'Enve m60'},
{'brand': 'Dt Swiss', 'spokes': 24, 'name': 'XM 320'},
{'brand': 'Dt Swiss', 'spokes': 32, 'name': 'XT 500'},
{'brand': 'Dt Swiss', 'spokes': 32, 'name': 'AR 122'},
{'brand': 'Dt Swiss', 'spokes': 24, 'name': 'XT 500'},
{'brand': 'Dt Swiss', 'spokes': 32, 'name': 'EX 551'},
{'brand': 'Derby', 'spokes': 24, 'name': 'Derby XC'},
{'brand': 'Derby', 'spokes': 32, 'name': 'Derby XC'},
{'brand': 'Derby', 'spokes': 24, 'name': 'Derby AM'},
{'brand': 'Derby', 'spokes': 32, 'name': 'Derby AM'},
{'brand': 'Derby', 'spokes': 24, 'name': 'Derby DH'},
{'brand': 'Derby', 'spokes': 32, 'name': 'Derby DH'}]

front_hubs_array=[{'brand':'DTSwiss', 'name':'DTSwiss 350', 'type':'front', 'axle':'15mm', 'disc':'iso', 'spoke':32},
     {'brand':'DTSwiss', 'name':'DTSwiss 240', 'type':'front', 'axle':'9mm', 'disc':'iso', 'spoke':24},
     {'brand':'DTSwiss', 'name':'DTSwiss 350', 'type':'front', 'axle':'15mm', 'disc':'direct', 'spoke':32},
     {'brand':'DTSwiss', 'name':'DTSwiss 240', 'type':'front', 'axle':'15mm', 'disc':'iso', 'spoke':24}]


rear_hubs_array=[{'brand':'DTSwiss', 'name':'DTSwiss 350', 'type':'rear', 'axle':'15mm', 'disc':'iso', 'spoke':32},
     {'brand':'DTSwiss', 'name':'DTSwiss 240', 'type':'rear', 'axle':'9mm', 'disc':'iso', 'spoke':24},
     {'brand':'DTSwiss', 'name':'DTSwiss 350', 'type':'rear', 'axle':'15mm', 'disc':'direct', 'spoke':32},
     {'brand':'DTSwiss', 'name':'DTSwiss 240', 'type':'rear', 'axle':'15mm', 'disc':'iso', 'spoke':24}]

rims = {}
fronthubs = {}
rearhubs = {}
for i,rim in enumerate(rims_array):
    rims[i] = rim

for i,hub in enumerate(front_hubs_array):
    fronthubs[i] = hub

for i,hub in enumerate(rear_hubs_array):
    rearhubs[i] = hub

data  = {'rims':rims, 'fronthubs':fronthubs, 'rearhubs':rearhubs}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
