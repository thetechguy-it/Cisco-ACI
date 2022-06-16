from acitoolkit.acitoolkit import *
import credentials

session = Session(credentials.url, credentials.user, credentials.pwd)
session.login()

file = open("data.txt", "r")
list_of_lists = []
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
    epg = EPG(splitted_list[4], app)
    bd.add_context(context)
    epg.add_bd(bd)
    #bd.set_unicast_route('yes')
    tenant.push_to_apic(session)
file.close()

#bd.set_arp_flood('yes')
#bd.set_unicast_route('no')
#bd.set_unknown_mac_unicast
#bd.set_unknown_multicast
#bd.set_unknown_unicast
#bd.add_subnet
#bd.set_multidestination