from acitoolkit.acitoolkit import *
import credentials

session = Session(credentials.url, credentials.user, credentials.pwd)
session.login()

new_tenant = "THETECHGUY"
new_app = "APP1"
new_vrf = "VRF1"
new_bd = "BD1"
new_epg = "EPG1"

tenant = Tenant(new_tenant)
app = AppProfile(new_app, tenant)
vrf = Context(new_vrf, tenant)
bd = BridgeDomain(new_bd, tenant)
epg = EPG(new_epg, app)
bd.add_context(vrf)
epg.add_bd(bd)

print(f"I'm going to push the following parameters\nTenant: {tenant}\nApplication Profile: {app}\nVRF: {vrf}\nBridge Domain: {bd}\nEPG: {epg}\n")
tenant.push_to_apic(session)
print("Configuration applied, please verify it through GUI")