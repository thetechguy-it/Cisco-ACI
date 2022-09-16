import acitoolkit.acitoolkit as aci
import credentials

session = aci.Session(credentials.url, credentials.user, credentials.pwd)
session.login()

file = open("data.txt", "r")
for line in file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    single_string = line_list[0]
    splitted_list = single_string.split(',')
    tenant = aci.Tenant(splitted_list[0])
    app = aci.AppProfile(splitted_list[1], tenant)
    vrf = aci.Context(splitted_list[2], tenant)
    bd = aci.BridgeDomain(splitted_list[3], tenant)
    if splitted_list[4] == '':
        print('!!! NOTE: THIS BD DOESN\'T HAVE A SUBNET !!!')
    else:
        bd_subnet = aci.Subnet(splitted_list[5], bd)
        bd_subnet.set_addr(splitted_list[4])
        bd_subnet.set_scope('public') #Set the 'Advertise Externally' on BD
        bd.add_subnet(bd_subnet)
    bd.set_unknown_mac_unicast('flood') #Enable ARP Flooding AND L2 Unknown Unicast 
    bd.set_arp_flood('yes')
    bd.set_unicast_route('no') #Disable the Unicast Routing function, the IP are 'disabled'. To activate change to 'yes'
    epg = aci.EPG(splitted_list[5], app)
    phydom = splitted_list[6]
    dom = aci.EPGDomain.get_by_name(session, phydom)
    bd.add_context(vrf)
    epg.add_bd(bd)
    epg.add_infradomain(dom)
    epgbddescr = splitted_list[7]
    epg.descr = epgbddescr
    bd.descr = epgbddescr
    print(f"I'm going to push the following parameters\nTenant: {tenant}\nApplication Profile: {app}\nVRF: {vrf}\nBridge Domain: {bd}\nEPG: {epg}\nPhysical Domain associated to EPG: {dom}\nEPG and BD Description: {epgbddescr}")    tenant.push_to_apic(session)
file.close()