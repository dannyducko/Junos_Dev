from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell

with Device(host='ENTER_IP_HERE', user='USERNAME_HERE', passwd='PASSWORD_HERE') as srx1:
    with StartShell(srx1) as ss:
        software_image = ss.run("ls -al /var/tmp/")
        print(software_image[1])

