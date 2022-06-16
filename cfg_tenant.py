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
    print(splitted_list)
    tenant = Tenant(splitted_list[0])
    app = AppProfile(splitted_list[1], tenant)
    context = Context(splitted_list[2], tenant)
    bd = BridgeDomain(splitted_list[3], tenant)
    bd_subnet = Subnet(splitted_list[5], bd)
    bd_subnet.set_addr(splitted_list[4])
    bd.add_subnet(bd_subnet)
    bd.set_unknown_mac_unicast('flood') #Enable ARP Flooding AND L2 Unknown Unicast 
    epg = EPG(splitted_list[5], app)
    bd.add_context(context)
    epg.add_bd(bd)
    tenant.push_to_apic(session)
file.close()