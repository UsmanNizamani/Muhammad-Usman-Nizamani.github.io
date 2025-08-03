# importing Allow list
import_file = "allow_list.txt"

# with open reading file

with open(import_file,"r") as file:
    ip_addresses=file.read()

# Convert string into list (one IP per line)

ip_addresses = ip_addresses.splitlines()

remove_list = ["10.0.0.5", "192.168.1.10","196.251.116.113","64.227.65.114"]

#Removing IPs that are in remove list from allow list

for ip in remove_list:
    if ip in ip_addresses:
        ip_addresses.remove(ip)

#storing updated ips
updated_ips = "\n".join(ip_addresses)

#overwrites the imported file with updated
with open(import_file,"w") as file:
    file.write(updated_ips)

