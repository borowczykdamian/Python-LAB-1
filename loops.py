ip_address=["192.168.1.1","10.0.0.1","172.16.0.1"]
for ip in ip_address:
    print(ip)

command="show ip interface brief"
for char in command:
    print(char)

interfaces={"GigabitEthernet0":"up","GigabitEthernet1":"down"}
for interface,status in interfaces.items():
    print(f"Interface {interface} is {status}")

for i in range(5):
    print(f"Interface GigabitEthernet0/{i}")

    