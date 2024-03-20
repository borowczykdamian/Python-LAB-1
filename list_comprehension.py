numbers=[1,2,3,4,5]
squares=[n**2 for n in numbers]

print(squares)


evens=[n for n in numbers if n%2==0]
odds=[n for n in numbers if n%2!=0]
print(evens)
print(odds)

ip_list=["192.168.1.1","10.0.0.256","172.16.0.1","256.0.0.1"]
valid_ips=[ip for ip in ip_list if all(0<=int(octet)<=255 for octet in ip.split('.'))]
print(valid_ips)

interfaces=[f"GigabitEthernet0/{i}" for i in range(0,5)]
print(interfaces)
