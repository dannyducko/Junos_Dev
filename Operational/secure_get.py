from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP


srx1 = Device(host='ENTER_IP_HERE', user='USERNAME_HERE', passwd='PASSWORD_HERE')

with SCP(srx1, progress=True) as scp:
    scp.get('/var/log/messages', local_path='../')

