from cgi import print_arguments
from acitoolkit.acitoolkit import *
import credentials

session = Session(credentials.url, credentials.user, credentials.pwd)
session.login()

tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)