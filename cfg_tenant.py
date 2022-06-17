from acitoolkit.acitoolkit import *
import credentials

session = Session(credentials.url, credentials.user, credentials.pwd)
session.login()
new_tenant = "THETECHGUY"
tenant = Tenant(new_tenant)
tenant.push_to_apic(session)

print("Configuration applied!\nNow let's check the Tenant list:")

tenantlist = Tenant.get(session)
for tenants in tenantlist:
    print(tenants.name)
if tenant.name == new_tenant:
    print(f"Congrats! Configuration applied successfully!\nTenant called {new_tenant} is in the list")    
else:
    print(f"Sorry! Tenant called {new_tenant} is not in the list, check your code and try again")