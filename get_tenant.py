from cgi import print_arguments
from acitoolkit.acitoolkit import *
import credentials

session = Session(credentials.url, credentials.user, credentials.pwd)
session.login()

tenantlist = Tenant.get(session)
for tenants in tenantlist:
    print(tenants.name)