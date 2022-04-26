from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='IP_HERE', user='USERNAME', passwd='PASSWORD') as srx1:
    with Config(srx1, mode='exclusive') as cu:
        print("Rolling back device configuration")
        cu.rollback(rb_id=1)
        cu.commit()
        print("Device configuration rolled back successfully")