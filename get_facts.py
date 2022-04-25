from jnpr.junos import Device
from pprint import pprint

srx2 = Device(host='ip_here', user='admin', passwd='pass')
srx1 = Device(host='ip_here', user='admin', passwd='pass')

what_device = input("What device would you like to query?\n1. srx1\n2. srx2\n > ")

if what_device == "1":
    srx1.open()
    pprint(srx1.facts)
    srx1.close()
else:
    srx2.open()
    pprint(srx2.facts)
    srx2.close()

exit()
