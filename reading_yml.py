import yaml
with open('network_config.yml','r') as file:
    network_config=yaml.safe_load(file)

print(network_config)
