from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='IP_HERE', user='USERNAME', passwd='PASSWORD') as srx1:
    with Config(srx1, mode="exclusive") as cu:
            cu.load(path="Configuration/confirm.conf", overwrite=True)
            cu.commit(confirm=5)
            print("Device configuration loaded successfully. \n Configuration will be rolled back in 5 minutes if it is not confirmed.")