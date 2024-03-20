import json

network_data={
    'switch':'Switch1',
    'ports':[
        {'name':'FastEthernet','vlan':'10'},
        {'name':'FastEthernet','vlan':'10'}
    ]
}

with open('new_network_config.json','w') as file:
    json.dump(network_data,file,indent=4)

    