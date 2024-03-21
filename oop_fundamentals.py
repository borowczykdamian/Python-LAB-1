class NetworkDevice:
    def __init__(self, hostname, ip_address):
        self.hostname=hostname
        self.ip_address=ip_address
    
    def display_config(self):
        print(f"Hostname: {self.hostname}, IP address: {self.ip_address}")

router1=NetworkDevice("Router1","192.168.1.1")
# print(f"Device: {router1.hostname}, IP: {router1.ip_address}")

router1.display_config()

print("\n")


class Router(NetworkDevice):
    def __init__(self,hostname,ip_address,routing_protocol):
        super().__init__(hostname,ip_address)
        self.routing_protocol=routing_protocol

    def display_config(self):
        super().display_config()
        print(f"Routing Protocol: {self.routing_protocol}")

router2=Router("Router1","192.168.1.1","OSPF")
# print(f"Routing Porotocol: {router2.routing_protocol}")

router2.display_config()
