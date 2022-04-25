from jnpr.junos import Device
from lxml import etree

# show version | display xml rpc
# show version | display xml
with Device(host='ENTER_IP_HERE', user='USERNAME_HERE', passwd='PASSWORD_HERE') as srx1:
    # Junos equivalant to Junos CLI "show version"
    sw = srx1.rpc.get_software_information({'format': 'text'})
    # Can change the above after .rpc. to whatever rpc you require.
    print(etree.tostring(sw, encoding='unicode', pretty_print='True'))
