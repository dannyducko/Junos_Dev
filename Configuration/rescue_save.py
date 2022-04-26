from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='IP_HERE', user='USERNAME', passwd='PASSWORD') as srx1:
    with Config(srx1, mode='exclusive') as cu:
        cu.rescue(action="save")
        # Above save can be ammended to delete, to delete the rescue config.
        print("Rescue configuration created successfully.")