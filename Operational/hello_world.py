from jnpr.junos import Device
from pprint import pprint
from getpass import getpass

junos_username = input("Device Username: ")
junos_password = input("Device Password: ")

dev = Device(host='ENTER_IP_HERE', user=junos_username, passwd=junos_password)

dev.open()
pprint(dev.facts)
dev.close()
