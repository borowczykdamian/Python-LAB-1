def greet():
    print("Hello, Network Engineer")

greet()


def configure_interface(interface_name,ip_address):     #czy trzeba deklarowac klase argumentow funkcji?
    print(f"Configuring {interface_name} with IP {ip_address}")

configure_interface("GigabitEthernet0/1","192.168.1.1")

configure_interface(ip_address="192.168.1.2",interface_name="GigabitEthernet0/1")

def calculate_metrics(bytes_transmitted,bytes_received):
    tx_rate=bytes_transmitted/60
    rx_rate=bytes_received/60
    return tx_rate, rx_rate

tx,rx=calculate_metrics(3000,5000)
print(f"Transmit Rate: {tx} Bps, Receive Rate: {rx} Bps")

def ping(host="8.8.8.8",count=4):
    print(f"Pinging {host} {count}")
    return "Ping successful"

