# with open('ip_addresses.txt','r') as file:
#     contents=file.read()
#     print(contents)

# with open('routing_table.txt','r') as file:
#     for line in file:
#         print(line.strip())

# subnet_masks=['255.255.255.0','255.255.0.0','255.0.0.0']
# with open('subnet_masks.txt','w') as file:
#     for mask in subnet_masks:
#         file.write(mask+'\n')


target_network='192.168.1.0/24'
with open('routing_table.txt','r') as file:
    for line in file:
        if target_network in line:
            print(line.strip())

