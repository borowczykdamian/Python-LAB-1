port_status="up"
if port_status=="up":
    print("The port is operational")

if port_status=="up":
    print("The port is operational")
else:
    print("The port is down")

port_speed=1000
if port_speed==100:
    print("FastEthernet port")
elif port_speed==1000:
    print("GigabitEthernet port")
else:
    print("Speed unrecognized")

interface_configs={
    "GigabitEthernet0/1":{"status":"up","vlan":"10"},
    "GigabitEthernet0/2":{"status":"down","vlan":"20"},
    "GigabitEthernet0/3":{"status":"up","vlan":"10"},
}

for interface_status in interface_configs.values():
    if interface_status['vlan']=="10":
        print(f"Vlan {interface_status['vlan']}")
