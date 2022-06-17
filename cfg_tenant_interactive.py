from acitoolkit.acitoolkit import *
import credentials

session = Session(credentials.url, credentials.user, credentials.pwd)
session.login()

file = open("data.txt", "r")
for line in file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    single_string = line_list[0]
    splitted_list = single_string.split(",")
    tenant = Tenant(splitted_list[0])
    app = AppProfile(splitted_list[1], tenant)
    context = Context(splitted_list[2], tenant)
    bd = BridgeDomain(splitted_list[3], tenant)
    if splitted_list[4] == "":
        print("!!! NOTE: THIS BD DOESN'T HAVE A SUBNET !!!")
    else:
        bd_subnet = Subnet(splitted_list[5], bd)
        bd_subnet.set_addr(splitted_list[4])
        bd.add_subnet(bd_subnet)
    bd.set_unknown_mac_unicast('flood') #Enable ARP Flooding AND L2 Unknown Unicast 
    epg = EPG(splitted_list[5], app)
    bd.add_context(context)
    epg.add_bd(bd)
    print("I'm going to push the following parameters: ")
    print(f"Tenant: {tenant}\nApplication Profile: {app}\nVRF: {context}\nBridge Domain: {bd}\nEPG: {epg}\n")
    result = input("Are you sure you want to proceed?[y/n]")
    if result == "y":
        tenant.push_to_apic(session)
        print("Configuration applied successfully!\n\n\n")
    elif result == "yes":
        tenant.push_to_apic(session)
        print("Configuration applied successfully!\n\n\n")
    else:
        continue
file.close()