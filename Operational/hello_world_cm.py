from jnpr.junos import Device
from pprint import pprint

# Below can be done with an SSH key, but i've manually added my credentials to lab.
with Device(host='ENTER_IP_HERE', user='USERNAME_HERE', passwd='PASSWORD_HERE') as srx1:
    # srx1.open()
    pprint(srx1.facts)
    # srx2.close()

