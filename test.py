import acitoolkit.acitoolkit as ACI
import credentials

# Define static values to pass (edit these if you wish to set differently)
TENANT_NAME = 'TENANT-001'
APP_NAME = 'APP-001'
EPG_NAME = 'EPG-001'
VLAN = {'name': 'vlan-5', 'encap_type': 'vlan', 'encap_id': '5'}
# Login to the APIC
session = ACI.Session(credentials.url, credentials.user, credentials.pwd)
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

# Create the Tenant, App Profile, and EPG
tenant = ACI.Tenant(TENANT_NAME)
app = ACI.AppProfile(APP_NAME, tenant)
epg = ACI.EPG(EPG_NAME, app)
vpcname = 'Heroes_FI-2A'    
vpc = ACI.PortChannel(vpcname)
epg.set_deployment_immediacy("immediate")

vlan_intf2 = ACI.L2Interface(VLAN['name'], VLAN['encap_type'], VLAN['encap_id'])
vlan_intf2.attach(vpc)
epg.attach(vlan_intf2)

tenant.push_to_apic(session)
# Push the tenant config to the APIC
