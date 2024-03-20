device={"hostname":"Router1",
        "ip":"192.168.1.1",
        "model":"Cisco 2901",
        "interfaces":["GigabitEthernet0","GigabitEthernet1"]}


print(device)

ip_address=device["ip"]
print(f"Device IP Address: {ip_address}")

device["location"]="Data Center A"
print(device)

device["ip"]="192.168.2.1"
print(device)

del device["model"]
location = device.pop("location")
print(device)
print(location)

print("\n")

for key in device.keys():
    print(key)

print("\n")

for value in device.values():
    print(value)

print("\n")

for key, value in device.items():
    print(f"{key}: {value}")

routing_table={
    "10.0.0.0/24":"192.168.1.1",
    "172.16.0.0/16":"192.168.2.1"
}

print("\n")

for network, next_hop in routing_table.items():
    print(f"Destination: {network}, Next Hop: {next_hop}")

