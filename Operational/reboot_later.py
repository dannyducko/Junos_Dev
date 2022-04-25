from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

device = input('Device IP: ')

with Device(host=device, user='USERNAME_HERE', passwd='PASSWORD_HERE') as dev:
    sw = SW(dev)
    print(sw.reboot(in_min=5))

# Clear the reboot on device with "clear system reboot"
