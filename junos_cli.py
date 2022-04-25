from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell

srx2 = Device(host='ip_here', user='admin', passwd='pass')
srx1 = Device(host='ip_here', user='admin', passwd='pass')

what_device = input("What device would you like to query?\n1. srx1\n2. srx2\n > ")
what_command = input("What command do you want to run?")
cli = f'cli -c "{what_command}"'

if what_device == "1":
    ss = StartShell(srx1)
    ss.open()
    command = ss.run(cli)
    print(command[1])
    ss.close()
else:
    ss = StartShell(srx2)
    ss.open()
    command = ss.run(cli)
    print(command[1])
    ss.close()

exit()
