from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='IP_HERE', user='USERNAME', passwd='PASSWORD') as srx1:
    with Config(srx1, mode='exclusive') as cu:
        rescue = cu.rescue(action="reload")
        if rescue is False:
            print("No rescue configuration exists on this device")
        else:
            cu.commit()
            print("Rescue configuration successfully committed.")